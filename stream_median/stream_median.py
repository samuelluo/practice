"""
Suppose integers are read from a data stream. For each additional element read
in, find the median so far.
"""

import heapq
# ---------------------------------------------------------
def stream_median(nums):
    # Set up
    left = []     # maxheap
                  # heapq is minheap by default; use negative numbers
    right = []    # minheap
    medians = []

    # Iterate
    for i in nums:
        # Determine the previous median
        if len(left) == 0:
            median = i
        else:
            median = medians[-1]

        # Depending on what the previous median was, push to left or right
        if i <= median:
            heapq.heappush(left, i*-1)
        elif i > median:
            heapq.heappush(right, i)

        # Rebalance left & right
        if len(right) > len(left):
            num = heapq.heappop(right)
            heapq.heappush(left, num*-1)
        elif len(left) > len(right)+1:
            num = heapq.heappop(left)
            heapq.heappush(right, num*-1)

        # Calculate & append the current median
        if len(left) == len(right):
            median = (left[0]*-1 + right[0])/2
        elif len(left) != len(right):
            median = left[0]*-1
        medians.append(median)

        # # Print
        # print(left)
        # print(right)
        # print(medians)
        # print()

    # Return
    return medians

# ---------------------------------------------------------
# Answer: [5, 7.5, 10, 7.5]
nums = [5, 10, 11, 1]
result = stream_median(nums)
print(result)

# Answer: [10, 9.5, 9, 8.5]
nums = [10, 9, 8, 7]
result = stream_median(nums)
print(result)