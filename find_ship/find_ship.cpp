// g++ -std=c++17 find_ship.cpp
/*
Suppose there is a battleship that starts at some X_0. At each time point, you
can check one location to see if the ship is there. However, the ship moves
S units at each time point. Devise a strategy for finding the ship.
*/

/*
Strategy: 2-dimensional radial search (clock-wise)
Note that (t, x0, s) map many-to-one to x_t.
There we cannot determine what x0 and s were once we find the ship.
t   x0   s   x_t = x0 + t*s
0    0   0    0
1   -1   0   -1
2   -1   1    1
3    0   1    3
4    1   1    5
5    1   0    1
*/

// Includes
#include <iostream>    // std::cout, std::endl
#include <random>      // std::random_device, std::uniform_int_distribution
#include <set>         // std::set

// Globals
std::random_device rd;

// ------------------------------------------------------------------
void find_ship(int X_0, int S) {
    // Set up
    int t = 0;         // time state
    int curr_x = 0;    // x0 guess
    int curr_y = 0;    // s guess
    int dir_x = 0;
    int dir_y = +1;
    std::set<std::pair<int, int>> checked;

    // Simulate
    while (true) {
        // If found, return
        int x_t = X_0 + t*S;
        int guess = curr_x + t*curr_y;
        if (x_t == guess) {
            std::cout << "Found!" << std::endl;
            std::cout << "t = " << t << std::endl;
            std::cout << "x_t = " << guess << std::endl;
            std::cout << "implied x_0 = " << curr_x << std::endl;
            std::cout << "implied s = " << curr_y << std::endl;
            return;
        }

        // Otherwise, check next in spiral
        t += 1;
        checked.insert(std::make_pair(curr_x, curr_y));
        curr_x += dir_x;
        curr_y += dir_y;

        // If turning right not in checked, change direction
        if (dir_x == 0 && dir_y == 1 &&
            checked.find(std::make_pair(curr_x + 1, curr_y + 0)) == checked.end()) {
            // std::cout << "now facing right" << std::endl;
            dir_x = +1;
            dir_y = 0;
        } else
        if (dir_x == 1 && dir_y == 0 &&
            checked.find(std::make_pair(curr_x + 0, curr_y - 1)) == checked.end()) {
            // std::cout << "now facing down" << std::endl;
            dir_x = 0;
            dir_y = -1;
        } else
        if (dir_x == 0 && dir_y == -1 &&
            checked.find(std::make_pair(curr_x - 1, curr_y + 0)) == checked.end()) {
            // std::cout << "now facing left" << std::endl;
            dir_x = -1;
            dir_y = 0;
        } else
        if (dir_x == -1 && dir_y == 0 &&
            checked.find(std::make_pair(curr_x + 0, curr_y + 1)) == checked.end()) {
            // std::cout << "now facing up" << std::endl;
            dir_x = 0;
            dir_y = +1;
        }
    }
}

int main() {
    int X_0;
    int S;

    X_0 = 5;
    S = 0;
    std::cout << "Battleship parameters: ";
    std::cout << "[" << X_0 << ", " << S << "]" << std::endl;
    find_ship(X_0, S);
    std::cout << std::endl;

    X_0 = std::uniform_int_distribution(-10, 10)(rd);
    S = std::uniform_int_distribution(-10, 10)(rd);
    std::cout << "Battleship parameters: ";
    std::cout << "[" << X_0 << ", " << S << "]" << std::endl;
    find_ship(X_0, S);
    std::cout << std::endl;
}
