// g++ -std=c++17 longest_substring_k_distinct_characters.cpp
/*
Given an integer k and a string s, find the length of the longest substring
that contains at most k distinct characters.
For example, given s = "abcba" and k = 2, the longest substring with k distinct
characters is "bcb".
*/
#include <string>
#include <map>
#include <iostream>
#include <vector>

int main() {
    std::string s = "abcba";
    int k = 2;

    int curr_left = 0; int curr_right = 0;
    int max_left = 0; int max_right = 0;
    std::map<char, int> char_counts;
    for (int i = 0; i < s.length(); i++) {
        // Update current count of characters 
        char char_i = s[i];
        curr_right += 1;
        if (char_counts.find(char_i) == char_counts.end()) {
            char_counts[char_i] = 0;
        } else {
            char_counts[char_i] += 1;
        }

        // Reduce current count of character if it has exceeded the limit k
        std::vector<char> keys;
        for (std::map<char, int>::iterator iter = char_counts.begin();
             iter != char_counts.end(); iter++) {
            if (iter->second != 0) {
                keys.push_back(iter->first);
                std::cout << iter->first << " ";
            }
        }
        std::cout << std::endl;
        
        while (keys.size() > k) {
            char_counts[s[curr_left]] -= 1;
            curr_left += 1;
        }

        // Compare current substring length to max & update
        if ((curr_right - curr_left) > (max_right - max_left)) {
            max_left = curr_left;
            max_right = curr_right;
        }
    }

    // Return
    std::cout << max_left << ", " << max_right << std::endl;
    std::cout << s.substr(max_left, max_right-max_left) << std::endl;
}