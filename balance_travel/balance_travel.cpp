// g++ -std=c++17 balance_travel.cpp
/*
Suppose there are interviewing N job candidates for roles in New York and
San Francisco.
There are two costs associated with each candidate, one for sending him/her to
each city.
Split the candidates into two equal-sized groups while also minimizing travel
cost.
*/

#include <algorithm>    // std::sort
#include <iostream>     // std::cout, std::endl
#include <tuple>        // std::tuple, std::make_tuple, std::tuple_cat
#include <vector>       // std::vector

// ------------------------------------------------------------------
bool cost_compare(const std::tuple<int, int, int> &a,
                  const std::tuple<int, int, int> &b) {
    return std::get<0>(a) > std::get<0>(b);
}

void balance_travel(std::vector<std::tuple<int, int>> costs) {
    // Set up
    std::vector<std::tuple<int, int, int>> swap_costs;
    for (auto i : costs) {
        std::tuple<int, int, int> swap_cost = std::make_tuple(
            std::get<0>(i) - std::get<1>(i),
            std::get<0>(i), std::get<1>(i));
        swap_costs.push_back(swap_cost);
    }
    std::sort(swap_costs.begin(), swap_costs.end(),
              [](std::tuple<int, int, int> a, std::tuple<int, int, int> b) {
        return std::abs(std::get<0>(a)) > std::abs(std::get<0>(b));
    });
    // for (auto i : swap_costs) {
    //     std::cout << std::get<0>(i) << " ";
    //     std::cout << std::get<1>(i) << " ";
    //     std::cout << std::get<2>(i) << std::endl;
    // }
    std::vector<std::tuple<int, int>> ny;
    std::vector<std::tuple<int, int>> sf;
    int i = 0;

    // Assign the largest cost differences (opportunity cost) first
    int threshold = costs.size()/2 + (costs.size() % 2 != 0);
    while (ny.size() < threshold && sf.size() < threshold) {
        std::tuple<int, int, int> swap_cost = swap_costs[i];
        std::tuple<int, int> cost = std::make_tuple(std::get<1>(swap_cost),
                                                    std::get<2>(swap_cost));
        if (std::get<0>(swap_cost) > 0) {    // If NY > SF, send to SF
            sf.push_back(cost);
        } else {                             // If NY < SF, send to NY
            ny.push_back(cost);
        }
        i += 1;
    }

    // Fill in the remaining slots
    while (ny.size() < costs.size()/2) {
        std::tuple<int, int, int> swap_cost = swap_costs[i];
        std::tuple<int, int> cost = std::make_tuple(std::get<1>(swap_cost),
                                                    std::get<2>(swap_cost));
        ny.push_back(cost);
        i += 1;
    }
    while (sf.size() < costs.size()/2) {
        std::tuple<int, int, int> swap_cost = swap_costs[i];
        std::tuple<int, int> cost = std::make_tuple(std::get<1>(swap_cost),
                                                    std::get<2>(swap_cost));
        sf.push_back(cost);
        i += 1;
    }

    // Print results
    int total_cost = 0;
    std::cout << "ny: [";
    for (auto i : ny) {
        std::cout << "("  << std::get<0>(i);
        std::cout << ", " << std::get<1>(i);
        std::cout << "), ";
        total_cost += std::get<0>(i);
    }
    std::cout << "]" << std::endl;

    std::cout << "sf: [";
    for (auto i : sf) {
        std::cout << "("  << std::get<0>(i);
        std::cout << ", " << std::get<1>(i);
        std::cout << "), ";
        total_cost += std::get<1>(i);
    }
    std::cout << "]" << std::endl;

    std::cout << "total cost: " << total_cost << std::endl;
    std::cout << std::endl;
}

int main() {
    std::vector<std::tuple<int, int>> costs;

    // Answer: 650
    costs = {
        std::make_tuple(400, 200),
        std::make_tuple(200, 100),
        std::make_tuple(300, 150),
        std::make_tuple(100, 50)
    };
    balance_travel(costs);

    // Answer: 1002
    costs = {
        std::make_tuple(1000, 1001),
        std::make_tuple(1, 11)
    };
    balance_travel(costs);

    // Answer: 1100
    costs = {
        std::make_tuple(1000, 1001),
        std::make_tuple(100, 99),
        std::make_tuple(1, 11)
    };
    balance_travel(costs);
}
