// g++ -std=c++17 k_sorted_lists.cpp
/*
Return a new sorted merged list from K sorted lists, each with size N.
*/
#include <vector>
#include <queue>
#include <iostream>

struct Nums {
    int value;
    int list_index;
    int element_index;
    bool operator<(const Nums& i) const {
        return value > i.value;
    }
};

std::vector<int> sort_lists(std::vector<std::vector<int>> lists) {
    std::priority_queue<Nums> min_heap;
    for (int list_index = 0; list_index < lists.size(); list_index++) {
        std::vector<int> list = lists[list_index];
        if (!list.empty()) {
            min_heap.push(Nums{list[0], list_index, 0});
        }
    }

    std::vector<int> merged;
    while (!min_heap.empty()) {
        auto[value, list_index, element_index] = min_heap.top();
        min_heap.pop();
        merged.push_back(value);
        if (element_index + 1 < lists[list_index].size()) {
            min_heap.push(Nums{lists[list_index][element_index + 1], list_index, element_index + 1});
        }
    }
    return merged;
}

int main() {
    std::vector<std::vector<int>> lists;
    std::vector<int> result;

    lists = {{10, 15, 30}, {12, 15, 20}, {17, 20, 32}};
    result = sort_lists(lists);
    for (auto i : result) {
        std::cout << i << " ";
    }
    std::cout << std::endl;

    lists = {{}, {}, {1, 2, 3}};
    result = sort_lists(lists);
    for (auto i : result) {
        std::cout << i << " ";
    }
    std::cout << std::endl;
}