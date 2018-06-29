// g++ -std=c++17 find_largest_subarray_sum.cpp
// Given an array of integers, find the continuous subarray that has the largest sum.
#include <vector>
#include <iostream>
#include <algorithm>

int largest_subarray_sum_1(std::vector<int> nums) {
    int curr_max = 0; int total_max = 0;
    for (auto i : nums) {
        curr_max = std::max(curr_max + i, i);
        total_max = std::max(curr_max, total_max);
    }
    return total_max;
}

std::pair<int, int> largest_subarray_sum_2(std::vector<int> nums) {
    int curr_left = 0; int curr_right = 0; int curr_max = nums[0];
    int total_left = 0; int total_right = 0; int total_max = nums[0];
    for (int i = 0; i < nums.size(); i++) {
        if (curr_max + nums[i] > nums[i]) {    // Extend the current array by one
            curr_max = curr_max + nums[i];
            curr_right += 1;
        } else {                   // Or, start a new array
            curr_max = nums[i];
            curr_left = i;
            curr_right = i;
        }

        if (curr_max > total_max) {
            total_max = curr_max;
            total_left = curr_left;
            total_right = curr_right;
        }
    }
    return std::pair<int, int>(total_left, total_right);
}

int main() {
    std::vector<int> nums = {-2, -3, 4, -1, -2, 1, 5, -3};
    int result_1 = largest_subarray_sum_1(nums);
    std::cout << result_1 << std::endl;    // Answer: 7

    std::pair<int, int> result_2 = largest_subarray_sum_2(nums);
    std::cout << "indexes: " << result_2.first << " " << result_2.second << std::endl;
    int subarray_sum = 0;
    std::cout << "subarray: ";
    for (int i = result_2.first; i <= result_2.second; i++) {
        std::cout << nums[i] << " ";
        subarray_sum += nums[i];
    }
    std::cout << std::endl;
    std::cout << "subarray_sum: " << subarray_sum << std::endl;
}