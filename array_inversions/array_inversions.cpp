// g++ -std=c++17 array_inversions.cpp
/*
We can determine how "out of order" an array A is by counting the number of
inversions it has. Two elements A[i] and A[j] form an inversion if A[i] > A[j]
but i < j. That is, a smaller element appears after a larger element.
*/

#include <iostream>    // std::cout, std::endl
#include <vector>      // std::vector

// ----------------------------------------------------------------------------
int array_inversions(std::vector<int> nums) {
    if (nums.size() <= 1) {
        return 0;
    } else {
        int mid = nums.size()/2;
        std::vector<int> left (nums.begin(), nums.begin() + mid);
        std::vector<int> right (nums.begin() + mid, nums.begin() + nums.size());
        int left_count = array_inversions(left);
        int right_count = array_inversions(right);

        int left_i = 0;
        int right_i = 0;
        int i = 0;
        int middle_count = 0;
        while (left_i < left.size() && right_i < right.size()) {
            if (left[left_i] < right[right_i]) {
                nums[i] = left[left_i];
                left_i += 1;
                i += 1;
            } else {
                nums[i] = right[right_i];
                middle_count += left.size() - left_i;
                right_i += 1;
                i += 1;
            }
        }
        while (left_i < left.size()) {
            nums[i] = left[left_i];
            left_i += 1;
            i += 1;
        }
        while (right_i < right.size()) {
            nums[i] = right[right_i];
            right_i += 1;
            i += 1;
        }
        return left_count + right_count + middle_count;
    }
}

// ----------------------------------------------------------------------------
int main() {
    std::vector<int> nums;
    int result;

    // Answer: 3
    nums = {2, 4, 1, 3, 5};
    result = array_inversions(nums);
    std::cout << result << std::endl;

    // Answer: 10
    nums = {5, 4, 3, 2, 1};
    result = array_inversions(nums);
    std::cout << result << std::endl;

    // Answer: 0
    nums = {1, 2, 3, 4, 5};
    result = array_inversions(nums);
    std::cout << result << std::endl;

    // Answer: 5
    nums = {1, 20, 6, 4, 5};
    result = array_inversions(nums);
    std::cout << result << std::endl;
}

