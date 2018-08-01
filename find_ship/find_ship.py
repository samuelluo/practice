"""
Suppose there is a battleship that starts at some X_0. At each time point, you
can check one location to see if the ship is there. However, the ship moves
S units at each time point. Devise a strategy for finding the ship.
"""

# Strategy: 2-dimensional radial search (clock-wise)
# Note that (t, x0, s) map many-to-one to x_t.
# There we cannot determine what x0 and s were once we find the ship.
# t   x0   s   x_t = x0 + t*s
# 0    0   0    0
# 1   -1   0   -1
# 2   -1   1    1
# 3    0   1    3
# 4    1   1    5
# 5    1   0    1

import random

# -------------------------------------------------------------------
def find_ship(X_0, S):
    # Set up
    t = 0
    curr_x = 0    # x0 guess
    curr_y = 0    # s guess
    dir_x = 0
    dir_y = +1
    checked = set() 

    # Simulate
    while True:
        x_t = X_0 + t*S
        guess = curr_x + t*curr_y
        if x_t == guess:
            print("Found!")
            print("t = {}".format(t))
            print("x_t = {}".format(guess))
            print("implied x_0 = {}".format(curr_x))
            print("implied s = {}".format(curr_y))
            break
        else:
            t += 1
            checked.add((curr_x, curr_y))
            curr_x += dir_x
            curr_y += dir_y
            if dir_x == 0 and dir_y == 1 and (curr_x + 1, curr_y + 0) not in checked:
                dir_x = +1
                dir_y = 0
            elif dir_x == 1 and dir_y == 0 and (curr_x + 0, curr_y - 1) not in checked:
                dir_x = 0
                dir_y = -1
            elif dir_x == 0 and dir_y == -1 and (curr_x - 1, curr_y + 0) not in checked:
                dir_x = -1
                dir_y = 0
            elif dir_x == -1 and dir_y == 0 and (curr_x + 0, curr_y + 1) not in checked:
                dir_x = 0
                dir_y = +1

# -------------------------------------------------------------------
X_0 = 5
S = 0
print("Battleship parameters: {}".format([X_0, S]))
find_ship(X_0, S)
print()

X_0 = random.randint(-10, 10)
S = random.randint(-10, 10)
print("Battleship parameters: {}".format([X_0, S]))
find_ship(X_0, S)
print()