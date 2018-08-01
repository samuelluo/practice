"""
Given a list of numbers, randomly shuffle the list.
Make sure each one of the N! permutations is equally likely.
"""

import random

nums = list(range(10))
for i in range(len(nums)):
    swap_index = random.randint(i, len(nums)-1)
    nums[i], nums[swap_index] = nums[swap_index], nums[i]
print(nums)