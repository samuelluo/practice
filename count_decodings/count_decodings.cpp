// g++ -std=c++17 count_decodings.cpp
// Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
// For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
#include <iostream>
#include <string>
#include <vector>

int count_decodings(std::string message) {
    // One decoding for a string of length 1
    // Initialize a base case of one decoding for string of length 0
    std::vector<int> ways = {1, 1};
    for (int i = 2; i < message.length()+1; i++) {
        // 1 decoding from string[:i-1] to string[:i]
        int ways_i = ways[i-1];

        // Convert right-most two chars into int
        std::string two_char = message.substr(i-2, 2);
        int two_char_num = std::stoi(two_char);
        
        // If the right-most two chars is within [1, 26],
        // then there is 1 additional decoding from string[:i-2] to string[:i]
        if (two_char_num >= 1 and two_char_num <= 26) {
            ways_i += ways[i-2];
        }
        ways.push_back(ways_i);
    }

    // Return
    return ways[message.length()];
}

int main() {
    std::string message;
    int result;

    message = "121";     // answer should be 3
    result = count_decodings(message);
    std::cout << result << std::endl;

    message = "135";     // answer should be 2
    result = count_decodings(message);
    std::cout << result << std::endl;

    message = "1234";    // answer should be 3
    result = count_decodings(message);
    std::cout << result << std::endl;
}