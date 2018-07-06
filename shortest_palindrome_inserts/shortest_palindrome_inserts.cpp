// g++ -std=c++17 shortest_palindrome_inserts.cpp
/*
Given a string, find the minimum number of characters that need to be 
inserted to form a palindrome.
*/
#include <string>
#include <iostream>
#include <algorithm>

// ----------------------------------------------------------------------------
int shortest_palindrome_inserts_1(std::string s) {
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
        return shortest_palindrome_inserts_1(s1);
    } else {
        std::string s1 = s.substr(0, (s.length()-1) - 0);
        std::string s2 = s.substr(1, (s.length()-0) - 1);
        return std::min(shortest_palindrome_inserts_1(s1),
                        shortest_palindrome_inserts_1(s2)) + 1;
    }
}

int shortest_palindrome_inserts_2(std::string s) {
    // inserts[i][j] = inserts for string[i:j]
    int inserts[s.length()+1][s.length()+1];
    memset(inserts, 0, sizeof(inserts));

    // Build bottom-up, from substrings of length 2 to substrings of length N.
    for (int l = 2; l < s.length()+1; l++) {
        for (int i = 0; i+l < s.length()+1; i++) {
            // std::cout << i    << " " << i+l      << "; ";
            // std::cout << s[i] << " " << s[i+l-1] << std::endl;
            if (s[i] == s[i+l-1]) {
                inserts[i][i+l] = inserts[i+1][i+l-1];
            } else {
                inserts[i][i+l] = std::min(inserts[i+0][i+l-1],
                                           inserts[i+1][i+l-0]) + 1;
            }
        }
    }

    /*
    // Check
    for (int i = 0; i < s.length()+1; i++) {
        for (int j = 0; j < s.length()+1; j++) {
            std::cout << inserts[i][j] << " ";
        }
        std::cout << std::endl;
    }
    */

    // Return inserts for full string
    return inserts[0][s.length()];
}

void shortest_palindrome_inserts(std::string s) {
    int result;
    std::cout << "string: " << s << std::endl;
    result = shortest_palindrome_inserts_1(s);
    std::cout << "minimum inserts method 1: " << result << std::endl;
    result = shortest_palindrome_inserts_2(s);
    std::cout << "minimum inserts method 2: " << result << std::endl;
}

// ----------------------------------------------------------------------------
int main() {
    std::string s;

    // 0 inserts
    s = "aba";
    shortest_palindrome_inserts(s);

    // 0 inserts
    s = "abba";
    shortest_palindrome_inserts(s);

    // 1 insert; 'abb' -> 'abba'
    s = "abb";
    shortest_palindrome_inserts(s);

    // 1 inserts; 'abab' -> 'ababa'
    s = "abab";
    shortest_palindrome_inserts(s);

    // 1 inserts; 'abca' -> 'acbca'
    s = "abca";
    shortest_palindrome_inserts(s);

    // 2 inserts; 'abcda' -> 'abdcda' -> 'abdcdba'
    s = "abbc";
    shortest_palindrome_inserts(s);

    // 2 inserts; 'abcda' -> 'abdcda' -> 'abdcdba'
    s = "abcda";
    shortest_palindrome_inserts(s);

    // 3 inserts; 'abcd' -> 'abcdc' -> 'abcdcb' -> 'abcdcba'
    s = "abcd";
    shortest_palindrome_inserts(s);
}
