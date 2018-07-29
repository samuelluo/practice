// g++ -std=c++17 stream_median.cpp
/*
Suppose integers are read from a data stream. For each additional element read
in, find the median so far.
*/

#include <functional>    // std::greater, std::less
#include <iostream>      // std::cout, std::endl
#include <queue>         // std::priority_queue
#include <vector>        // std::vector
#include <typeinfo>      // typeid

// ----------------------------------------------------------------------------
template <typename T> void print_vector(T& v) {
    std::cout << "[";
    for (int i = 0; i < v.size(); i++) {
        if (i == v.size() - 1) {
            std::cout << v[i];
        } else {
            std::cout << v[i] << ", ";
        }
    }
    std::cout << "]" << std::endl;
}

template <typename T> void print_queue(T q) {
    std::cout << "[";
    while (!q.empty()) {
        std::cout << q.top();
        q.pop();
        if (!q.empty()) {
            std::cout << ", ";
        }
    }
    std::cout << "]" << std::endl;
}

// template <typename T> void print(T var) {
//     if (typeid(var) == typeid(std::vector<T>)) {
//         print_vector(var);
//     }
//     if (typeid(var) == typeid(std::priority_queue<T>)) {
//         print_queue(var);
//     }
// }

std::vector<double> stream_median(std::vector<int> nums) {
    // Set up
    std::vector<double> medians;
    std::priority_queue<int, std::vector<int>, std::less<int>> left;        // maxheap
    std::priority_queue<int, std::vector<int>, std::greater<int>> right;    // minheap

    // Iterate
    for (auto i : nums) {
        // Determine the previous median
        double median;
        if (left.empty()) {
            median = 0.0;
        } else {
            median = medians.back();
        }

        // Depending on what the previous median was, push to left or right
        if (i <= median) {
            left.push(i);
        } else if (i > median) {
            right.push(i);
        }

        // Rebalance left & right; left/right differ by at most 1
        if (right.size() > left.size()) {
            int num = right.top();
            right.pop();
            left.push(num);
        } else if (left.size() > right.size()+1) {
            int num = left.top();
            left.pop();
            right.push(num);
        }

        // Calculate & append the current median
        if (left.size() == right.size()) {
            median = (left.top() + right.top())/2.0;
        } else if (left.size() != right.size()) {
            median = left.top();
        }
        medians.push_back(median);

        /*
        // Print
        print_queue(left);
        print_queue(right);
        print_vector(medians);
        std::cout << std::endl;
        */
    }

    // Return
    return medians;
}

// ----------------------------------------------------------------------------
int main() {
    std::vector<int> nums;
    std::vector<double> result;

    // Answer: [5, 7.5, 10, 7.5]
    nums = {5, 10, 11, 1};
    result = stream_median(nums);
    print_vector(result);

    // Answer: [10, 9.5, 9, 8.5]
    nums = {10, 9, 8, 7};
    result = stream_median(nums);
    print_vector(result);
}