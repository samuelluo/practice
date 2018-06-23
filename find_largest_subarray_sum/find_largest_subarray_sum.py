def largest_subarray_sum(nums):
    curr_max = total_max = nums[0]
    for i in nums:
        curr_max = max(curr_max + i, i)   # Either add to subarray, or start a new subarray
        # print(curr_max)
        total_max = max(total_max, curr_max)
    return total_max

def largest_subarray_sum_2(nums):
    """ left_index & right_index inclusive """
    curr_left = curr_right = 0
    total_left = total_right = 0
    curr_max = total_max = nums[0]

    for i in range(len(nums)):
        if curr_max + nums[i] > nums[i]:
            curr_max = curr_max + nums[i]
            curr_right += 1
        else:
            curr_max = nums[i]
            curr_left = curr_right = i
        # print([curr_max, curr_left, curr_right])
        
        if total_max < curr_max:
            total_left = curr_left
            total_right = curr_right
            total_max = curr_max
    return [total_left, total_right]


nums = [-2, -3, 4, -1, -2, 1, 5, -3]
result = largest_subarray_sum(nums)
print(result)
result = largest_subarray_sum_2(nums)
subarray = nums[result[0]:result[1]+1]
subsum = sum(subarray)
print([result, subarray, subsum])