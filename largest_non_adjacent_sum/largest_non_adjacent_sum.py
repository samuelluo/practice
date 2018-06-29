"""
Given a list of integers, write a function that returns the largest sum of
non-adjacent numbers. Numbers can be 0 or negative.
For example:
[2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5.
[5, 1, 1, 5] should return 10, since we pick 5 and 5.
"""

# --------------------------------------------------
def largest_non_adjacent_sum(nums):
    largest = [[nums[0], [0]]]
    if nums[1] > nums[0]: largest.append([nums[1], [1]])
    else:                 largest.append([nums[0], [0]])
    for i in range(2, len(nums)):
        if largest[i-2][0] + nums[i] > largest[i-1][0]:
            largest_sum = largest[i-2][0] + nums[i]
            indexes = largest[i-2][1] + [i]
            largest.append([largest_sum, indexes])
        else:
            largest.append(largest[i-1])
    return largest
    
def largest_non_adjacent_sum_2(nums):
    curr_largest = prev_largest = 0
    for i in nums:
        if prev_largest + i > curr_largest:
            old_prev_largest = prev_largest
            prev_largest = curr_largest
            curr_largest = old_prev_largest + i
        else:
            prev_largest = curr_largest
        # print([prev_largest, curr_largest])
    return curr_largest

# --------------------------------------------------
# largest = [[5, [0]], [6, [1]], [6, [1]], [7, [1, 3]]]
nums = [5, 6, 1, 1]
print(largest_non_adjacent_sum(nums))
print(largest_non_adjacent_sum_2(nums))

# largest = [[5, [0]], [5, [0]], [6, [0, 2]], [6, [0, 2]]]
nums = [5, 1, 1, 1]
print(largest_non_adjacent_sum(nums))
print(largest_non_adjacent_sum_2(nums))

# largest = [5, 5, 6, 10]
nums = [5, 1, 1, 5]
print(largest_non_adjacent_sum(nums))
print(largest_non_adjacent_sum_2(nums))

# largest = [2, 4, 8, 8, 13]
nums = [2, 4, 6, 2, 5]
print(largest_non_adjacent_sum(nums))
print(largest_non_adjacent_sum_2(nums))