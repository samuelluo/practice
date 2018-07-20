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

# ---------------------------------------------------------
def walls_and_water_1(walls):
    """ O(n^2) """
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

def walls_and_water_2(walls):
    """ O(3*n) = O(n) """
    water = [0]
    left = walls.copy()
    right = walls.copy()

    for i in range(1, len(walls)):
        left[i] = max(left[i-1], left[i])
    for i in range(len(walls)-2, -1, -1):
        right[i] = max(right[i+1], right[i])

    for i in range(len(walls)):
        water.append(water[i] + min(left[i], right[i]))

    print(walls)
    print(left)
    print(right)
    print([min(left[i], right[i]) for i in range(len(left))])
    print(water)

# ---------------------------------------------------------
walls = [1, 2, 1, 3, 1, 2, 3, 1]
# walls_and_water_1(walls)
walls_and_water_2(walls)
