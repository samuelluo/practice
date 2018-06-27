"""
Given a value N and a list of coin types C, find the number of coin combinations 
that sum up to N.
For example, for N=4 and C=[1,2,3], there are four combinations:
[1,1,1,1], [1,1,2], [1,3], [2,2]
"""

# ----------------------------------------
def coin_combinations(N, C):
    """
    Given target N, coins list C, and new coin C':
    ways = ways(N, coins) + \       # Num ways to N without C'
           ways(N-C', coins+[C'])   # Num ways to N-C' using all coins
    
    Written top-down, instead of bottoms-up:
    ways = ways(N, C[:-1]) + \   # Num ways to N without C'
           ways(N-C[-1], C)      # Num ways to N-C' using all coins
    
    If coins can't reach N (ex: N=1, C=[2]), then this set reduces to:
    ways(N=1, C=[]) + \   # zero ways with zero coins
    ways(N=-1, C=[2])     # zero ways to a negative target
    """
    if N < 0 or len(C) == 0:
        return 0
    if N == 0:
        return 1
    else:
        return coin_combinations(N, C[:-1]) + \
               coin_combinations(N - C[-1], C)

# ----------------------------------------
def coin_combinations_2(N, C):
    """
    Use a bottoms-up approach, starting from N=1 and C=C[0]
    ways[i][j] = coin #i, target j
    """
    # Create ways table
    ways = [[0 for j in range(N+1)] for i in range(len(C))]
    
    # Initialize base case N == 0
    for i in range(len(C)):
        ways[i][0] = 1
    
    # Fill
    for i in range(len(C)):
        for j in range(1, N+1):
            if i-1 >= 0:
                ways[i][j] += ways[i-1][j]
            if j-C[i] >= 0:
                ways[i][j] += ways[i][j-C[i]]
    # print(ways)
    
    # Return
    return ways[len(C)-1][N]

# ----------------------------------------
# Answer: 4
N = 4
C = [1,2,3]
result = coin_combinations(N, C)
print(result)
result = coin_combinations_2(N, C)
print(result)

# Answer: 5
N = 10
C = [2,5,3,6]
result = coin_combinations(N, C)
print(result)
result = coin_combinations_2(N, C)
print(result)