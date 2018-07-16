"""
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
"""

import collections

# ---------------------------------------------------------
def subarray_maximums_1(nums, k):
    """ O(n*k) """
    print("[", end="")
    for i in range(k, len(nums)+1):    # O(N+1-k)
        sub = nums[i-k:i]
        print(max(sub), end=", ")    # O(k)
    print("]")

def subarray_maximums_2(nums, k):
    """ O(2*n) = O(n); every num is added once, removed once """
    queue = collections.deque()
    max_list = []
    for i in range(len(nums)):
        # Remove indexes outside of current window, from the left
        while len(queue) != 0 and queue[0] <= i-k:
            queue.popleft()

        # Remove nums smaller than the current num, from the right
        while len(queue) != 0 and nums[i] >= nums[queue[-1]]:
            queue.pop()
            
        # Add current num, to the right
        queue.append(i)
        
        # Append to subarray maximums
        # print([[i-k, i], nums[queue[0]]])
        max_list.append(nums[queue[0]])

    # Print
    print(max_list[k-1:])

# ---------------------------------------------------------
nums = [10, 5, 2, 7, 8, 7]
k = 3
subarray_maximums_1(nums, k)
subarray_maximums_2(nums, k)

nums = [1, 2, 3, 4, 2, 3, 5]
k = 3
subarray_maximums_1(nums, k)
subarray_maximums_2(nums, k)
