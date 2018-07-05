// g++ -std=c++17 estimate_pi.cpp
/*
The area of a circle is defined as πr^2. Estimate π to 3 decimal places.
*/
#include <iostream>
#include <cmath>

int main() {
    srand(time(NULL));
    int inside = 0;
    int total = 1000000;
    for (int i = 0; i < total; i++) {
        double x = double(rand()) / RAND_MAX;
        double y = double(rand()) / RAND_MAX;
        if (std::pow(x, 2) + std::pow(y, 2) <= 1) {
            inside += 1;
        }
    }
    double pi = double(inside) / total * 4;
    std::cout << pi << std::endl;
}