"""
Given an integer k and a string s, find the length of the longest substring
that contains at most k occurrences of any given character.
For example, given s = "abcbabc" and k = 2, the longest substring with k distinct
characters is "abcba".
"""

# ---------------------------------------------------------
def longest_substring_k_occurrences(s, k):
    curr_left = curr_right = 0
    max_left = max_right = 0
    char_counts = {}    # {char : count}
    for i in range(len(s)):
        # Update curr
        char = s[i]
        curr_right += 1
        if char not in char_counts.keys():
            char_counts[char] = 1
        else:
            char_counts[char] += 1
            if char_counts[char] > k:
                processed = False
                while not processed:
                    if s[curr_left] == char:
                        processed = True
                    char_counts[s[curr_left]] = max(0, char_counts[s[curr_left]]-1)
                    curr_left += 1
        # print([curr_left, curr_right])
        # print(char_counts)

        # Update max
        if (curr_right - curr_left) > (max_right - max_left):
            max_left = curr_left
            max_right = curr_right

    # Return
    return [max_left, max_right]

# ---------------------------------------------------------
s = 'abcbabc'
k = 2
max_left, max_right = longest_substring_k_occurrences(s, k)
print([max_left, max_right, s[max_left:max_right]])

s = 'abcbbaacba'
k = 2
max_left, max_right = longest_substring_k_occurrences(s, k)
print([max_left, max_right, s[max_left:max_right]])
