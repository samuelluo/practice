// g++ -std=c++17 testing.cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<std::vector<int>> nums = {{1}, {1}};
    for (auto& v : nums) {
        for (std::vector<int>::iterator it = v.begin();
             it != std::end(v); ) {
            it = v.erase(it);
        }
    }
    std::cout << nums.size() << std::endl;

    std::cout << "[";
    for (auto& v : nums) {
        std::cout << "[";
        for (auto& i : v) {
            std::cout << i << " " << std::endl;
        }
        std::cout << "], ";
    }
    std::cout << "]" << std::endl;
}