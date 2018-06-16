def num_ways_1(N):
    if N == 1: return 1   # 1 way: [1]
    if N == 2: return 2   # 2 ways: [1+1, 2]
    return num_ways_1(N-1) + num_ways_1(N-2)   # take one step from N-1, or 2 steps from N-2

def num_ways_2(N):
    if N in [0, 1]: return 1
    ways = [1, 1]
    for i in range(2, N+1):
        ways.append(ways[i-1] + ways[i-2])
    return ways[N]

def num_ways_3(N, X):
    if N == 0: return 1
    ways = [1]
    for i in range(1, N+1):
        ways_i = 0
        for j in X:
            if i-j >= 0:
                ways_i += ways[i-j]
        ways.append(ways_i)
    return ways[N]

N = 3
print(num_ways_1(N))
print(num_ways_2(N))

X = [2,4]
print(num_ways_3(N, X))
X = [1,2,3]
print(num_ways_3(N, X))