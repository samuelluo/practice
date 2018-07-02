// g++ -std=c++17 coin_combinations.cpp
/*
Given a value N and a list of coin types C, find the number of coin combinations 
that sum up to N.
For example, for N=4 and C=[1,2,3], there are four combinations:
[1,1,1,1], [1,1,2], [1,3], [2,2]
*/
#include <iostream>
#include <vector>

// --------------------------------------------------------
int coin_combinations_1(int N, std::vector<int> C) {
    /*
    Given target N, coins list C, and new coin C':
    ways = ways(N, coins) + \       # Number of ways to N without C'
           ways(N-C', coins+[C'])   # Number of ways to N-C' using all coins
    
    Written top-down, instead of bottoms-up:
    ways = ways(N, C[:-1]) + \   # Number of ways to N without C'
           ways(N-C[-1], C)      # Number of ways to N-C' using all coins
    
    If coins can't reach N (ex: N=1, C=[2]), then this set reduces to:
    ways(N=1, C=[]) + \   # Zero ways with zero coins
    ways(N=-1, C=[2])     # Zero ways to a negative target
    */
    if (N < 0 || C.size() == 0) {
        return 0;
    }
    if (N == 0) {
        return 1;
    }
    else {
        std::vector<int> C_without(C.begin(), C.begin() + C.size()-1);
        int without = coin_combinations_1(N, C_without);
        int with    = coin_combinations_1(N - C[C.size()-1], C);
        return without + with;
    }
}

int coin_combinations_2(int N, std::vector<int> C) {
    /*
    Use a bottoms-up approach, starting from N=1 and C=C[0]
    ways[i][j] = coin #i, target=j
    */
    // Create ways table; len(C) vectors of size N+1
    std::vector<std::vector<int>> ways(C.size(), std::vector<int>(N+1));

    // Initialize base case N == 0
    for (int i = 0; i < C.size(); i++) {
        ways[i][0] = 1;
    }
    
    // Fill
    for (int i = 0; i < C.size(); i++) {
        for (int j = 1; j < N+1; j++) {
            if (i-1 >= 0)
                ways[i][j] += ways[i-1][j];
            if (j-C[i] >= 0)
                ways[i][j] += ways[i][j-C[i]];
        }
    }

    // Return
    return ways[C.size()-1][N];
}

// --------------------------------------------------------
int main() {
    int N; std::vector<int> C; int result;

    // Answer: 4
    N = 4;
    C = {1,2,3};
    result = coin_combinations_1(N, C);
    std::cout << result << std::endl;
    result = coin_combinations_2(N, C);
    std::cout << result << std::endl;

    // Answer: 5
    N = 10;
    C = {2,5,3,6};
    result = coin_combinations_1(N, C);
    std::cout << result << std::endl;
    result = coin_combinations_2(N, C);
    std::cout << result << std::endl;
}
