// g++ -std=c++17 shortest_palindrome_inserts.cpp
// Given a string, find the minimum number of characters that need to be 
// inserted to form a palindrome.
#include <string>
#include <iostream>
#include <algorithm>

int shortest_palindrome_inserts(std::string s) {
    if (s.length() <= 1) {
        return 0;
    }
    if (s.length() == 2) {
        if (s[0] != s[s.length()-1]) {
            return 1;
        } else {
            return 0;
        }
    }
    if (s[0] == s[s.length()-1]) {
        std::string s1 = s.substr(1, (s.length()-1) - 1);
        return shortest_palindrome_inserts(s1);
    } else {
        std::string s1 = s.substr(0, (s.length()-1) - 0);
        std::string s2 = s.substr(1, (s.length()) - 1);
        return std::min(shortest_palindrome_inserts(s1),
                        shortest_palindrome_inserts(s2)) + 1;
    }
}

int main() {
    std::string s;
    int result;

    // 0 inserts
    s = "aba";
    result = shortest_palindrome_inserts(s);
    std::cout << result << std::endl;

    // 0 inserts
    s = "abba";
    result = shortest_palindrome_inserts(s);
    std::cout << result << std::endl;

    // 1 insert; 'abb' -> 'abba'
    s = "abb";
    result = shortest_palindrome_inserts(s);
    std::cout << result << std::endl;

    // 1 inserts; 'abab' -> 'ababa'
    s = "abab";
    result = shortest_palindrome_inserts(s);
    std::cout << result << std::endl;

    // 1 inserts; 'abca' -> 'acbca'
    s = "abca";
    result = shortest_palindrome_inserts(s);
    std::cout << result << std::endl;

    // 2 inserts; 'abcda' -> 'abdcda' -> 'abdcdba'
    s = "abbc";
    result = shortest_palindrome_inserts(s);
    std::cout << result << std::endl;

    // 2 inserts; 'abcda' -> 'abdcda' -> 'abdcdba'
    s = "abcda";
    result = shortest_palindrome_inserts(s);
    std::cout << result << std::endl;

    // 3 inserts
    s = "abcd";
    result = shortest_palindrome_inserts(s);
    std::cout << result << std::endl;
}
