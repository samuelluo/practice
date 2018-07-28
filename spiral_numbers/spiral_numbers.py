
# ---------------------------------------------------------
def spiral_numbers_1(N):
    nums = [[0 for i in range(N)] for i in range(N)]
    c1 = r1 = 0
    c2 = r2 = N-1
    val = 1
    while c1 < c2 and r1 < r2:
        for i in range(c1, c2 + 1):
            nums[r1][i] = val
            val += 1
        r1 += 1
        for i in range(r1, r2 + 1):
            nums[i][c2] = val
            val += 1
        c2 -= 1
        for i in range(c2, c1-1, -1):
            nums[r2][i] = val
            val += 1
        r2 -= 1
        for i in range(r2, r1-1, -1):
            nums[i][c1] = val
            val += 1
        c1 += 1
    return nums

def pretty_print(nums):
    max_num = max([max(row) for row in nums])
    max_spaces = len(str(max_num))

    for row in nums:
        for i in row:
            len_i = len(str(i))
            end_spaces = " " * (max_spaces - len_i)
            print(i, end=end_spaces + " ")
        print()

# ---------------------------------------------------------
N = 4
result = spiral_numbers_1(N)
pretty_print(result)