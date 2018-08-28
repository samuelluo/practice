"""
We can determine how "out of order" an array A is by counting the number of
inversions it has. Two elements A[i] and A[j] form an inversion if A[i] > A[j]
but i < j. That is, a smaller element appears after a larger element.
"""

# -----------------------------------------------------------------------------
def array_inversions(nums):
    if len(nums) <= 1:
        return [nums, 0]
    else:
        mid = len(nums)//2
        left = nums[:mid]
        right = nums[mid:]
        left, left_count = array_inversions(left)
        right, right_count = array_inversions(right)

        left_i = right_i = i = middle_count = 0
        while left_i < len(left) and right_i < len(right):
            if left[left_i] < right[right_i]:
                nums[i] = left[left_i]
                left_i = left_i + 1
                i += 1
            else:
                nums[i] = right[right_i]
                middle_count += len(left) - left_i
                right_i = right_i + 1
                i += 1

        while left_i < len(left):
            nums[i] = left[left_i]
            left_i = left_i + 1
            i += 1
        while right_i < len(right):
            nums[i] = right[right_i]
            right_i = right_i + 1
            i += 1
        return [nums, left_count + right_count + middle_count]

# -----------------------------------------------------------------------------
# Answer: 3
nums = [2, 4, 1, 3, 5]
result = array_inversions(nums)
print(result)

# Answer: 10
nums = [5, 4, 3, 2, 1]
result = array_inversions(nums)
print(result)

# Answer: 0
nums = [1, 2, 3, 4, 5]
result = array_inversions(nums)
print(result)

# Answer: 5
nums = [1, 20, 6, 4, 5]
result = array_inversions(nums)
print(result)
