"""
Suppose there are N machines, each with a list of random integers.
Find a way to calculate the median across the different machines.
"""

import random

# ---------------------------------------------------------
def find_element_k(nums, k):
    while True:
        # Remove empty lists
        nums = [i for i in nums if len(i) != 0]

        # Find number of element less than a random pivot element
        machine_i = random.randint(0, len(nums)-1)
        element_i = random.randint(0, len(nums[machine_i])-1)
        element = nums[machine_i][element_i]
        num_lte = [len([j for j in i if j <= element]) for i in nums]
        num_lte = sum(num_lte)
        num_e = [len([j for j in i if j == element]) for i in nums]
        num_e = sum(num_e)
        num_elements = [len(i) for i in nums]
        num_elements = sum(num_elements)
        # print([nums, element, num_lte, num_e, num_elements])

        # Current pivot element is the kth element
        if num_lte == k or num_e == num_elements:
            return element
        # Current pivot is too small
        # The number of less-than elements we are expecting should also decrease
        elif num_lte <= k:
            nums = [[j for j in i if j > element] for i in nums]
            k -= num_lte
        # Current pivot element is too large
        # Removing elements larger than the pivot does not affect num_lte
        elif num_lte > k:
            nums = [[j for j in i if j <= element] for i in nums]

def distributed_median(nums):
    # Out of 7 elements, median is element #4
    num_elements = [len(i) for i in nums]
    num_elements = sum(num_elements)
    if num_elements % 2 != 0:
        i = find_element_k(nums, num_elements//2+1)
        return i
    else:
        i1 = find_element_k(nums, num_elements//2+1)
        i2 = find_element_k(nums, num_elements//2)
        return (i1+i2)/2

def exact_median(nums):
    flattened = []
    for i in nums:
        for j in i:
            flattened.append(j)
    flattened = sorted(flattened)
    if len(flattened) % 2 != 0:
        i = flattened[len(flattened)//2]
        return i
    else:
        i1 = flattened[len(flattened)//2]
        i2 = flattened[len(flattened)//2 - 1]
        return (i1+i2)/2

# ---------------------------------------------------------
nums = [[1,2,3], [4], [5,6,7]]
result = exact_median(nums)
print("Exact median: {}".format(result))
result = distributed_median(nums)
print("Distributed median: {}".format(result))
print()

nums = [[1,2,3], [4], [5,6,7,8]]
result = exact_median(nums)
print("Exact median: {}".format(result))
result = distributed_median(nums)
print("Distributed median: {}".format(result))
print()

nums = [[1], [1]]
result = exact_median(nums)
print("Exact median: {}".format(result))
result = distributed_median(nums)
print("Distributed median: {}".format(result))
print()

num_machines = random.randint(10, 20)
num_elements = random.choices(range(10), k=num_machines)
nums = [[random.randint(0, 1000) for j in range(i)] for i in num_elements]
result = exact_median(nums)
print("Exact median: {}".format(result))
result = distributed_median(nums)
print("Distributed median: {}".format(result))
print()
