// g++ -std=c++17 subset_sum.cpp
/*
Given a list of numbers and a number k, return whether a subset of the
numbers from the list add up to k.
*/
#include <iostream>
#include <map>
#include <set>
#include <vector>

// ------------------------------------------------------------------
bool subset_sum_1(std::vector<int> nums, int k, int length) {
    if (k == 0) {
        return true;
    }
    if (length == 0 and k != 0) {
        return false;
    }

    bool not_included = subset_sum_1(nums, k, length-1);
    bool included = false;
    if (nums[length-1] <= k) {
        included = subset_sum_1(nums, k-nums[length-1], length-1);
    }
    return (included || not_included);
}

std::vector<int> subset_sum_2(std::vector<int> nums, int k) {
    // table[i][j] = does nums[0:i] have a subset that adds up to j?
    // table[0][0] = nums=[], target=0
    bool table[nums.size()+1][k+1];
    memset(table, false, sizeof(table));

    // Fill in the base cases
    table[0][0] = true;
    for (int i = 1; i <= nums.size(); i++) {
        table[i][0] = true;    // use an empty subset to get to target=0
    }
    for (int j = 1; j <= k; j++) {
        table[0][j] = false;    // empty subset cannot reach any non-zero target
    }

    // Iterate
    for (int i = 1; i <= nums.size(); i++) {    // nums_i = nums[0:i]
        for (int j = 1; j <= k; j++) {    // target = j
            bool not_include = table[i-1][j];    // don't include nums[i] to get to target j
            bool include = false;
            if (j >= nums[i-1]) {
                include = table[i-1][j-nums[i-1]];    // do include nums[i] to get to target j
                                                      // or: nums[0:i-1] to get to target j-nums[i-1]
            }
            table[i][j] = not_include || include;
        }
    }

    /*
    // Check
    for (int i = 0; i <= nums.size(); i++) {
        for (int j = 0; j <= k; j++) {
            std::cout << table[i][j] << " ";
        }
        std::cout << std::endl;
    }
    */

    // Return
    std::vector<int> indexes;
    if (table[nums.size()][k] == true) {
        int i = nums.size(); int j = k;
        while (i != 0 && j != 0) {
            bool not_included = table[i-1][j];
            bool included     = table[i-1][j-nums[i-1]];
            if (not_included == true) {
            } else {
                indexes.push_back(i-1);
                j = j-nums[i-1];
            }
            i = i-1;
        }
    }
    return indexes;
}

void subset_sum(std::vector<int> nums, int k) {
    std::cout << "nums = [";
    for (int i = 0; i < nums.size(); i++) {
        if (i != nums.size()-1)
            std::cout << i << ", ";
        else
            std::cout << i << "]; ";
    }
    std::cout << "k = " << k << std::endl;

    // subset sum method 1
    int length = nums.size();
    bool result = subset_sum_1(nums, k, length);
    std::cout << "method 1: " << std::endl;
    if (result == true) {
        std::cout << k << " in nums" << std::endl;
    } else {
        std::cout << k << " not in nums" << std::endl;
    }

    // subset sum method 2
    std::vector<int> indexes = subset_sum_2(nums, k);
    std::cout << "method 2: " << std::endl;
    if (indexes.size() != 0) {
        std::cout << "indexes: ";
        for (auto i : indexes) {
            std::cout << i << " ";
        }
        std::cout << std::endl;
        std::cout << "nums: ";
        for (auto i : indexes) {
            std::cout << nums[i] << " ";
        }
        std::cout << std::endl;
    } else {
        std::cout << k << " not in nums" << std::endl;
    }
    std::cout << std::endl;
}
// ------------------------------------------------------------------
int main() {
    std::vector<int> nums;
    int k;

    nums = {3, 34, 4, 12, 5, 2};
    k = 11;
    subset_sum(nums, k);

    nums = {1, 2, 3, 3};
    k = 6;
    subset_sum(nums, k);
}
