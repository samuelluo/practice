"""
Given n non-negative integers representing an elevation map where the width of 
each bar is 1, compute how much water it is able to trap after raining.

For example, the following set of walls would be represented by the array of 
numbers below:

      |     |
  |   |   | |
|_|_|_|_|_|_|_|

[1, 2, 1, 3, 1, 2, 3, 1]
"""

walls = [1, 2, 1, 3, 1, 2, 3, 1]
water = [0]

for i in range(1, len(walls)):
    wall_i = walls[i]
    prev_max_i = i-1
    for j in range(i-1, -1, -1):
        if walls[j] > walls[prev_max_i]:
            prev_max_i = j
    height = min(wall_i, walls[prev_max_i])
    width = i - prev_max_i
    curr_water = height * width
    water.append(curr_water + water[prev_max_i])

print(water)