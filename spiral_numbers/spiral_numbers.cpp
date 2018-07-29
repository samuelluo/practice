// g++ -std=c++17 spiral_numbers.cpp

#include <iostream>    // std::cout, std::endl
#include <array>       // std::array
#include <string>      // std::to_string

void pretty_print(int* M, int N) {
    // Determine max string length that needs to be accounted for
    int max_num = 0;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            int curr_num = *(M + i*N + j);
            int len_i = std::to_string(curr_num).length();
            std::cout << len_i << " ";
            if (curr_num > max_num) {
                max_num = curr_num;
            }
        }
        std::cout << std::endl;
    }
    int max_spaces = std::to_string(max_num).length();
    std::cout << max_spaces << std::endl;
    std::cout << std::endl;

    // Print
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            int curr_num = *(M + i*N + j);
            int len_i = std::to_string(curr_num).length();
            std::string end_spaces = std::string(max_spaces - len_i, ' ');
            std::cout << curr_num << end_spaces << " ";
        }
        std::cout << std::endl;
    }
}

int main() {
    // Set up
    int N = 4;
    int M[N][N];
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            M[i][j] = 0;
        }
    }

    // Fill
    int curr_r = 0;
    int curr_c = 0;
    int dir_r = 0;
    int dir_c = +1;
    M[curr_r][curr_c] = 1;
    int val = 2;
    while (val <= N*N) {
        if (curr_r + dir_r < N && curr_c + dir_c < N &&
            curr_r + dir_r >= 0 && curr_r + dir_c >= 0 &&
            M[curr_r + dir_r][curr_c + dir_c] == 0) {
            M[curr_r + dir_r][curr_c + dir_c] = val;
            val += 1;
            curr_r += dir_r;
            curr_c += dir_c;
        } else {
            if (dir_r == 0 && dir_c == 1) {
                dir_r = 1;
                dir_c = 0;
            }
            else if (dir_r == 1 && dir_c == 0) {
                dir_r = 0;
                dir_c = -1;
            }
            else if (dir_r == 0 && dir_c == -1) {
                dir_r = -1;
                dir_c = 0;
            }
            else if (dir_r == -1 && dir_c == 0) {
                dir_r = 0;
                dir_c = 1;
            }
        }
    }
    pretty_print(*M, N);
}
