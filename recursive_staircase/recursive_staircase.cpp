// g++ -std=c++14 recursive_staircase.cpp
#include <cstdlib>
#include <iostream>
#include <vector>

int num_ways_1(int N) {
    if (N == 1) return 1;
    if (N == 2) return 2;
    return num_ways_1(N-1) + num_ways_1(N-2);
}

int num_ways_2(int N) {
    std::vector<int> ways = {1, 1};
    for (int i = 2; i < N+1; i++) {
        ways.push_back(ways[i-1] + ways[i-2]);
    }
    return ways[N];
}

int num_ways_3(int N, std::vector<int> X) {
    std::vector<int> ways = {1};   // Base case: 1 way to get to 0
    for (int i = 1; i < N+1; i++) {
        int ways_i = 0;
        for (int j : X) {
            if (i-j >= 0) {
                ways_i += ways[i-j];
            }
        }
        ways.push_back(ways_i);
    }
    return ways[N];
}

int main() {
    int N = 3;
    std::cout << num_ways_1(N) << std::endl;
    std::cout << num_ways_2(N) << std::endl;

    N = 3;
    std::vector<int> X = {1, 2, 3};
    std::cout << num_ways_3(N, X) << std::endl;   // [3], [1, 2], [2, 1], [1, 1, 1]

    N = 1;
    X = {2, 3};
    std::cout << num_ways_3(N, X) << std::endl;
    return 0;
}