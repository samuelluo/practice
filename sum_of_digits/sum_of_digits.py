"""
Given an integer value n, find out the n-th positive integer whose sum of 
digits is 10.
For example, given 1, you should return 19. Given 2, you should return 28.
"""

# -----------------------------------------------
def sum_of_digits(n):
    i = 1
    num = 19
    nums = [num]
    while i != n:
        # Increment
        num -= 1
        num += 10

        # Calculate sum of digits
        digits_sum = 0
        digits = num
        while digits != 0:
            digits_sum += digits % 10
            digits = digits // 10

        # Check if sum meets criteria
        if digits_sum == 10:
            i += 1
            nums.append(num)

    # Return
    return nums

# -----------------------------------------------
n = 20
result = sum_of_digits(n)
print(result)