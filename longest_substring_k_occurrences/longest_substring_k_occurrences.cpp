// g++ -std=c++17 longest_substring_k_occurrences.cpp
/*
Given an integer k and a string s, find the length of the longest substring
that contains at most k occurrences of any given character.
For example, given s = "abcbabc" and k = 2, the longest substring with k distinct
characters is "abcba".
*/

#include <iostream>    // std::cout, std::endl
#include <map>         // std::map
#include <string>      // std::string

// ---------------------------------------------------------
std::pair<int, int> longest_substring_k_occurrences(std::string s, int k) {
    int curr_left = 0;
    int curr_right = 0;
    int max_left = 0;
    int max_right = 0;
    std::map<char, int> char_counts;    // {char : count}
    for (int i = 0; i < s.size(); ++i) {
        // Update curr
        char curr_char = s[i];
        curr_right += 1;
        if (char_counts.find(curr_char) == char_counts.end()) {
            char_counts[curr_char] = 1;
        } else {
            char_counts[curr_char] += 1;
            if (char_counts[curr_char] > k) {
                bool processed = false;
                while (!processed) {
                    if (s[curr_left] == curr_char) {
                        processed = true;
                    }
                    char_counts[s[curr_left]] = std::max(0, char_counts[s[curr_left]]-1);
                    curr_left += 1;
                }
            }
        }

        // Update max
        if ((curr_right - curr_left) > (max_right - max_left)) {
            max_left = curr_left;
            max_right = curr_right;
        }
    }
    return std::make_pair(max_left, max_right);
}

// ---------------------------------------------------------
int main() {
    std::string s;
    int k;
    int max_left;
    int max_right;

    // Answer: [0, 5, 'abcba']
    s = "abcbabc";
    k = 2;
    std::tie(max_left, max_right) = longest_substring_k_occurrences(s, k);
    std::cout << "[";
    std::cout << max_left << ", ";
    std::cout << max_right << ", ";
    std::cout << "'" << s.substr(max_left, max_right-max_left) << "'";
    std::cout << "]" << std::endl;

    // Answer: [2, 8, 'cbbaac']
    s = "abcbbaacba";
    k = 2;
    std::tie(max_left, max_right) = longest_substring_k_occurrences(s, k);
    std::cout << "[";
    std::cout << max_left << ", ";
    std::cout << max_right << ", ";
    std::cout << "'" << s.substr(max_left, max_right-max_left) << "'";
    std::cout << "]" << std::endl;
}

