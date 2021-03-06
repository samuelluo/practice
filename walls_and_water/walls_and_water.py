"""
Given n non-negative integers representing an elevation map where the width of 
each bar is 1, compute how much water it is able to trap after raining.

For example, the following set of walls would be represented by the array of 
numbers below:

[1, 2, 1, 3, 1, 2, 3, 1]

      |     |
  |   |   | |
|_|_|_|_|_|_|_|

or: 

   |  |
 | | ||
||||||||
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
    """ O(4*n) = O(n) """
    left = walls.copy()
    for i in range(1, len(walls)):
        left[i] = max(left[i-1], left[i])
    
    right = walls.copy()
    for i in range(len(walls)-2, -1, -1):
        right[i] = max(right[i+1], right[i])
    
    heights = [min(left[i], right[i]) for i in range(len(left))]
    
    water = [0]
    for i in range(1, len(walls)):
        water.append(water[i-1] + min(heights[i], heights[i-1]))
    print(water)

def walls_and_water_3(walls):
    """ Another interpretation: water accumulates on top of walls """
    """ O(3*n) = O(n) """
    left = walls.copy()
    for i in range(1, len(walls)):
        left[i] = max(left[i-1], left[i])
    
    right = walls.copy()
    for i in range(len(walls)-2, -1, -1):
        right[i] = max(right[i+1], right[i])
    
    water = [0]
    for i in range(1, len(walls)):
        water.append(water[i-1] + min(left[i], right[i]) - walls[i])
    print(water)

# ---------------------------------------------------------
"""
Answer: 15
      |     |
  |   |   | |
|_|_|_|_|_|_|_|

Answer: 4
   |  |
 | | ||
||||||||
"""
walls = [1, 2, 1, 3, 1, 2, 3, 1]
walls_and_water_1(walls)
walls_and_water_2(walls)
walls_and_water_3(walls)
print()

"""
Answer: 15
..........|
|         |
|     |   |
|_._._|_._|

Answer: 10
.....|
|    |
|  | |
|__|_|
"""
walls = [3, 0, 0, 2, 0, 4]
walls_and_water_1(walls)
walls_and_water_2(walls)
walls_and_water_3(walls)
print()