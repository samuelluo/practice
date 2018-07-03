// g++ -std=c++17 reverse_sentence.cpp
/*
Given a sentence, reverse the order of the words.
For example, given an input string be “foo bar baz”, the function should return
“baz bar foo”.
*/
#include <iostream>

void reverse(char* sentence) {
    // Reverse each word in sentence
    char* start_i = NULL;
    char* end_i = sentence;
    while (*end_i != '\0') {
        if (start_i == NULL && *end_i != ' ') {
            start_i = end_i;
        }
        if (start_i != NULL &&
            (*(end_i+1) == ' ' || *(end_i+1) == '\0')) {
            char temp;
            char* left_i = start_i;
            char* right_i = end_i;
            while(left_i < right_i) {
                temp = *left_i;
                *left_i = *right_i;
                *right_i = temp;
                left_i += 1;
                right_i -= 1;
            }
            start_i = NULL;
        }
        end_i += 1;
    }
    
    // Reverse sentence
    char temp;
    char* left_i = sentence;
    char* right_i = end_i-1;
    while(left_i < right_i) {
        temp = *left_i;
        *left_i = *right_i;
        *right_i = temp;
        left_i += 1;
        right_i -= 1;
    }
}

int main() {
    char sentence[] = "cat in a hat";
    std::cout << sentence << " -> "; 
    reverse(sentence);
    std::cout << sentence << std::endl;
}
