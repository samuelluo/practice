"""
Suppose integers are read from a data stream. For each additional element read
in, find the median so far.
"""

import heapq

# Answer: [5, 7.5, 10, 7.5]
nums = [5, 10, 11, 1]

left = []     # maxheap; heapq is minheap by default; use negative numbers
right = []    # minheap
medians = []
for i in nums:
    if len(left) == 0:
        median = i
    if i <= median:
        heapq.heappush(left, i*-1)
    elif i > median:
        heapq.heappush(right, i)

    if len(right) > len(left):
        num = heapq.heappop(right)
        heapq.heappush(left, num*-1)

    if len(left) == 0:
        median = i
    elif len(left) == len(right):
        median = (left[0]*-1 + right[0])/2
    elif len(left) != len(right):
        median = left[0]*-1
    medians.append(median)

print(medians)