// g++ -std=c++17 largest_non_adjacent_sum.cpp
/*
Given a list of integers, write a function that returns the largest sum of
non-adjacent numbers. Numbers can be 0 or negative.
For example:
[2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5.
[5, 1, 1, 5] should return 10, since we pick 5 and 5.
*/

#include <vector>      // std::vector
#include <iostream>    // std::cout, std::endl

int largest_non_adjacent_sum(std::vector<int> nums) {
    int curr_largest = 0;
    int prev_largest = 0;
    for (auto i : nums) {
        // Use the current number, skip an index, compare to current largest
        // If it is larger, update
        if (prev_largest + i > curr_largest) {
            int old_prev_largest = prev_largest;
            prev_largest = curr_largest;
            curr_largest = old_prev_largest + i;
        }
        // Otherwise, maintain current largest value & update previous largest value
        // The previous largest can move forward one index
        else {
            prev_largest = curr_largest;
        }
    }
    return curr_largest;
}

int main() {
    std::vector<int> nums;
    int result;

    // largest = 13
    nums = {2, 4, 6, 2, 5};
    result = largest_non_adjacent_sum(nums);
    std::cout << result << std::endl;

    // largest = 10
    nums = {5, 1, 1, 5};
    result = largest_non_adjacent_sum(nums);
    std::cout << result << std::endl;

    // largest = [[5, [0]], [6, [1]], [6, [1]], [7, [1, 3]]]
    nums = {5, 6, 1, 1};
    result = largest_non_adjacent_sum(nums);
    std::cout << result << std::endl;

    // largest = [[5, [0]], [5, [0]], [6, [0, 2]], [6, [0, 2]]]
    nums = {5, 1, 1, 1};
    result = largest_non_adjacent_sum(nums);
    std::cout << result << std::endl;
}