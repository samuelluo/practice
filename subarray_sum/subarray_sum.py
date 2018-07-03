"""
Given an integer array, find if there is a continuous subarray that sums up to
a target value k.
"""

# --------------------------------------------------
def subarray_sum(nums, k):
    # start_index inclusive, end_index not inclusive
    start_index = end_index = curr_sum = 0
    for i in nums:
        end_index += 1
        curr_sum += i
        while curr_sum > k:
            curr_sum -= nums[start_index]
            start_index += 1
        if curr_sum == k:
            return [start_index, end_index]
    return None

# --------------------------------------------------
nums = [1, 4, 20, 3, 10, 5]
k = 33
result = subarray_sum(nums, k)
if result is not None:
    print([result, nums[result[0]:result[1]]])
else:
    print([result, None])
    
nums = [1, 4, 20, 3, 10, 5]
k = 32
result = subarray_sum(nums, k)
if result is not None:
    print([result, nums[result[0]:result[1]]])
else:
    print([result, None])