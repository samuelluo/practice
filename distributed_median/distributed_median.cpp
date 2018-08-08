// g++ -std=c++17 distributed_median.cpp
/*
Suppose there are N machines, each with a list of random integers.
Find a way to calculate the median across the different machines.
*/

#include <iostream>    // std::cout, std::endl
#include <random>      // std::random_device, std::mt19937,
                       // std::uniform_int_distribution
#include <vector>      // std::vector

std::random_device rd;

// ------------------------------------------------------------------
template<typename T>
void print_nums(T& v) {
    std::cout << "[";
    for (int i = 0; i < v.size(); i++) {
        std::cout << "[";
        for (int j = 0; j < v[i].size(); ++j) {
            if (j == v[i].size() - 1) {
                std::cout << v[i][j];
            } else {
                std::cout << v[i][j] << ", ";
            }
        }
        if (i == v.size() - 1) {
            std::cout << "]";
        } else {
            std::cout << "], ";
        }
    }
    std::cout << "]" << std::endl;
}

// ------------------------------------------------------------------
double find_element_k(std::vector<std::vector<int>> nums, int k) {
    while (true) {
        // Remove empty lists
        for (std::vector<std::vector<int>>::iterator it = nums.begin();
             it != std::end(nums); ) {
            if (it->size() == 0) {
                it = nums.erase(it);
            } else {
                ++it;
            }
        }

        // Randomly select a pivot element
        int machine_i = std::uniform_int_distribution<int>(0, nums.size()-1)(rd);
        int element_i = std::uniform_int_distribution<int>(0, nums[machine_i].size()-1)(rd);
        double element = nums[machine_i][element_i];

        // Find number of element less than a random pivot element
        int num_lte = 0;
        int num_e = 0;
        int num_elements = 0;
        for (auto& v : nums) {
            for (auto& i : v) {
                if (i <= element) {
                    num_lte += 1;
                }
                if (i == element) {
                    num_e += 1;
                }
                num_elements += 1;
            }
        }
        // print_nums(nums);
        // std::cout << element << ", ";
        // std::cout << num_lte << ", ";
        // std::cout << k << ", ";
        // std::cout << num_e << ", ";
        // std::cout << num_elements << std::endl;

        // Current pivot element is the kth element
        if (num_lte == k || num_e == num_elements) {
            return element;
        }
        // Current pivot is too small
        // The number of less-than elements we are expecting should also decrease
        else if (num_lte <= k) {
            for (auto& v : nums) {
                for (std::vector<int>::iterator it = v.begin();
                     it != std::end(v); ) {
                    if (*it <= element) {
                        it = v.erase(it);
                    } else {
                        ++it;
                    }
                }
            }
            k -= num_lte;
        }
        // Current pivot element is too large
        // Removing elements larger than the pivot does not affect num_lte
        else if (num_lte > k) {
            for (auto& v : nums) {
                for (std::vector<int>::iterator it = v.begin();
                     it != std::end(v); ) {
                    if (*it > element) {
                        it = v.erase(it);
                    } else {
                        ++it;
                    }
                }
            }
        }
    }
}

double distributed_median(std::vector<std::vector<int>> nums) {
    // Calculate the number of elements
    int num_elements = 0;
    for (auto& v : nums) {
        num_elements += v.size();
    }

    // Calculate median
    if (num_elements % 2 != 0) {
        double i = find_element_k(nums, num_elements/2 + 1);
        return i;
    } else {
        double i1 = find_element_k(nums, num_elements/2 + 1);
        double i2 = find_element_k(nums, num_elements/2);
        return (i1+i2)/2;
    }
}

double exact_median(std::vector<std::vector<int>> nums) {
    // Flatten & sort
    std::vector<int> flattened;
    for (auto& v : nums) {
        for (auto& i : v) {
            flattened.push_back(i);
        }
    }
    std::sort(flattened.begin(), flattened.end());

    // Calculate median
    if (flattened.size() % 2 != 0) {
        double i = flattened[flattened.size()/2];
        return i;
    } else {
        double i1 = flattened[flattened.size()/2];
        double i2 = flattened[flattened.size()/2 - 1];
        return (i1+i2)/2;
    }
}

// ------------------------------------------------------------------
int main() {
    // Set up
    std::vector<std::vector<int>> nums;
    double result;

    // Answer: 4
    nums = {{4}, {1,2,3}, {5,6,7}};
    result = exact_median(nums);
    std::cout << "Exact median: " << result << std::endl;
    result = distributed_median(nums);
    std::cout << "Distributed median: " << result << std::endl;
    std::cout << std::endl;

    // Answer: 4.5
    nums = {{1,2,3}, {4}, {5,6,7,8}};
    result = exact_median(nums);
    std::cout << "Exact median: " << result << std::endl;
    result = distributed_median(nums);
    std::cout << "Distributed median: " << result << std::endl;
    std::cout << std::endl;

    // Answer: 1.0
    nums = {{1}, {1}};
    result = exact_median(nums);
    std::cout << "Exact median: " << result << std::endl;
    result = distributed_median(nums);
    std::cout << "Distributed median: " << result << std::endl;
    std::cout << std::endl;
}