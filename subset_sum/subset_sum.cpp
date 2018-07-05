// g++ -std=c++17 subset_sum.cpp
/*
Given a list of numbers and a number k, return whether a subset of the
numbers from the list add up to k.
*/
#include <iostream>
#include <map>
#include <set>
#include <vector>

bool subset_sum(std::vector<int> nums, int k, int length) {
    if (k == 0) {
        return true;
    }
    if (length == 0 and k != 0) {
        return false;
    }

    bool not_included = subset_sum(nums, k, length-1);
    bool included = false;
    if (nums[length-1] <= k) {
        included = subset_sum(nums, k-nums[length-1], length-1);
    }
    return (included || not_included);
}

int main() {
    std::vector<int> nums = {1, 4, 45, 6, 10, -8};
    int k = 100;
    int length = nums.size();
    bool result = subset_sum(nums, k, length);
    if (result == true) {
        std::cout << k << " in nums" << std::endl;
    } else {
        std::cout << k << " not in nums" << std::endl;
    }
}