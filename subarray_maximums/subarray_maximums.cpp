// g++ -std=c++17 subarray_maximums.cpp
/*
Given an array of integers and a number k, where 1 <= k <= length of the array,
compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3,
we should get: [10, 7, 8, 8], since:
10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)

Do this in O(n) time and O(k) space. You can modify the input array in-place
and you do not need to store the results. You can simply print them out as you
compute them.
*/

#include <deque>       // std::deque
#include <iostream>    // std::cout, std::endl
#include <vector>      // std::vector

std::vector<int> subarray_maximums(std::vector<int> nums, int k) {
    std::deque<int> queue;
    std::vector<int> max_list;
    for (int i = 0; i < nums.size(); i++) {
        // Remove indexes outside of current window, from the front
        while (queue.size() != 0 && queue.front() <= i-k) {
            queue.pop_front();
        }

        // Remove nums smaller than the current num, from the back
        while (queue.size() != 0 && nums[i] >= nums[queue.back()]) {
            queue.pop_back();
        }

        // Add current num, to the right
        queue.insert(queue.end(), i);

        // Append to subarray maximums
        max_list.push_back(nums[queue.front()]);
    }
    std::vector<int>::iterator begin = max_list.begin() + k-1;
    std::vector<int>::iterator end   = max_list.end();
    return std::vector<int>(begin, end);
}

int main() {
    std::vector<int> nums;
    int k;
    std::vector<int> result;

    // Answer: [10, 7, 8, 8]
    nums = {10, 5, 2, 7, 8, 7};
    k = 3;
    result = subarray_maximums(nums, k);
    for (auto i : result) {
        std::cout << i << ", ";
    }
    std::cout << std::endl;

    // Answer: [3, 4, 4, 4, 5]
    nums = {1, 2, 3, 4, 2, 3, 5};
    k = 3;
    result = subarray_maximums(nums, k);
    for (auto i : result) {
        std::cout << i << ", ";
    }
    std::cout << std::endl;
}