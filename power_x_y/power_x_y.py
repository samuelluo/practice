"""
Given two integers x and y, write a function to compute x^y. 
"""

# ---------------------------------------------------------
def power_1(x, y):
    """ x^y, x & y are integers?
        time complexity: O(y) """
    result = 1
    for i in range(abs(y)): result *= x
    if y < 0: result = 1/result
    return result

def power_2(x, y):
    """ O(log y), does not support a negative exponent """
    if (y == 0):
        return 1
    
    val = power_2(x, y//2)
    if int(y % 2) == 0:
        return val * val
    else:
        return x * val * val

def power_3(x, y):
    """ O(log y), supports negative exponent """
    if y == 0: return 1
    
    # x^y = x^(y/2) * x^(y/2) * (x if odd else 1)
    val = power_3(x, int(y/2))   # Want exponent closest to 0
                                 # double-slash divide does not work
    if y % 2 == 0:
        return 1 * val * val
    else:
        if y > 0:
            return x * val * val
        else:
            return (1/x) * val * val

def power_4(x, y):
    """ O(log y), iterative """
    result = 1
    while y > 0:
        if y % 2 == 1: # If exponent is odd, add one X to result
            result *= x
        y = int(y/2) # Cut y in half; cut remaining exponent in half
        x = x * x    # Double the number of Xs; double the result's exponent 
    return result

# ---------------------------------------------------------
# 0.5^2 = 0.25
x, y = 0.5, 2
print("\n({})^({})".format(x, y))
result = power_1(x, y)
print(result)
result = power_2(x, y)
print(result)

# (-2)^3 = -8
x, y = -2, 3
print("\n({})^({})".format(x, y))
result = power_1(x, y)
print(result)
result = power_2(x, y)
print(result)

# 2^-2 = 1/4 = 0.25
x, y = 2, -3
print("\n({})^({})".format(x, y))
result = power_1(x, y)
print(result)
result = power_3(x, y)
print(result)

# 3^5 = 243
x, y = 3, 5
print("\n({})^({})".format(x, y))
result = power_1(x, y)
print(result)
result = power_3(x, y)
print(result)
result = power_4(x, y)
print(result)