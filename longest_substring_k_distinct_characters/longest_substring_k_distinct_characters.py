"""
Given an integer k and a string s, find the length of the longest substring
that contains at most k distinct characters.
For example, given s = "abcba" and k = 2, the longest substring with k distinct
characters is "bcb".
"""

# ---------------------------------------------------------
def longest_substring_k_distinct_characters(s, k):
    curr_left = curr_right = 0
    max_left = max_right = 0
    char_counts = {}
    for i in range(len(s)):
        # Update curr
        char = s[i]
        curr_right += 1
        if char not in char_counts.keys():
            char_counts[char] = 1
        else:
            char_counts[char] += 1

        # Reduce curr
        while len(char_counts.keys()) > k:
            if char_counts[s[curr_left]] == 1:
                char_counts.pop(s[curr_left])
            else:
                char_counts[s[curr_left]] -= 1
            curr_left += 1

        # Update max
        if (curr_right - curr_left) > (max_right - max_left):
            max_left = curr_left
            max_right = curr_right
        # print([curr_left, curr_right, char_counts])

    # Return
    return [max_left, max_right]


# ---------------------------------------------------------
# Answer: bcb
s = 'abcba'
k = 2
max_left, max_right = longest_substring_k_distinct_characters(s, k)
print([max_left, max_right, s[max_left:max_right]])

# Answer: bcbb
s = 'abcbbaacba'
k = 2
max_left, max_right = longest_substring_k_distinct_characters(s, k)
print([max_left, max_right, s[max_left:max_right]])
