// g++ -std=c++14 find_two_elements_sum.cpp
#include <iostream>
#include <map>
#include <set>
#include <vector>

bool find_two_elements_sum(std::vector<int> nums, int k) {
    std::set<int> nums_set;
    for (auto i : nums) {
        int remainder = k - i;
        if (nums_set.find(remainder) != nums_set.end()) {
            return true;
        }
        nums_set.insert(i);
    }
    return false;
}

/* If there are two elements in nums that sum up to k,
   return two-element vector {index_1, index_2} */
std::vector<int> find_two_elements_sum_2(std::vector<int> nums, int k) {
    std::map<int, int> nums_map;    // <num, index>
    std::vector<int> result;
    for (int i = 0; i < nums.size(); i++) {
        int remainder = k - nums[i];
        if (nums_map.find(remainder) != nums_map.end()) {
            result = {nums_map[remainder], i};
            return result;
        } else {
            nums_map[nums[i]] = i;
        }
    }
    return result;
}

int main() {
    std::vector<int> nums = {1, 4, 45, 6, 10, -8};
    int k = 16;
    bool result = find_two_elements_sum(nums, k);
    if (result == true) {
        std::cout << k << " in nums" << std::endl;
    } else {
        std::cout << k << " not in nums" << std::endl;
    }

    std::vector<int> result_2 = find_two_elements_sum_2(nums, k);
    if (result_2.size() != 0) {
        std::cout << k << " in nums" << std::endl;
        std::cout << "indexes: ";
        for (auto i : result_2) {
            std::cout << i << ' ';
        }
        std::cout << std::endl;
        std::cout << "values: ";
        for (auto i : result_2) {
            std::cout << nums[i] << ' ';
        }
    } else {
        std::cout << k << " not in nums" << std::endl;
    }
}