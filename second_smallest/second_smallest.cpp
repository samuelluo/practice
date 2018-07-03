// g++ -std=c++14 find_second_smallest.cpp
/*
Given an integer array, find the second smallest value.
*/
#include <iostream>
#include <limits>
#include <vector>

std::vector<int> find_second_smallest(std::vector<int> nums) {
    int first = std::numeric_limits<int>::max();
    int second = std::numeric_limits<int>::max();
    std::vector<int> results;
    for (auto i : nums) {
        if (i < first) {
            second = first;
            first = i;
        } else if (i > first and i < second) {
            second = i;
        }
    }
    if (first != std::numeric_limits<int>::max()) results.push_back(first);
    if (second != std::numeric_limits<int>::max()) results.push_back(second);
    return results;
}

int main() {
    std::vector<int> nums = {5, 5, 4, 3};
    std::vector<int> results = find_second_smallest(nums);
    for (auto i : nums) {
        std::cout << i << " ";
    }
    std::cout << std::endl;
    if (results.size() != 2) {
        std::cout << "No second smallest" << std::endl;
    } else {
        std::cout << "Second smallest: " << results[1] << std::endl;
    }
    
    nums = {2, 2, 2};
    results = find_second_smallest(nums);
    for (auto i : nums) {
        std::cout << i << " ";
    }
    std::cout << std::endl;
    if (results.size() != 2) {
        std::cout << "No second smallest" << std::endl;
    } else {
        std::cout << "Second smallest: " << results[1] << std::endl;
    }
}