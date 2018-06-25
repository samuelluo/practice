"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
"""

def count_decodings(message):
    ways = [1, 1]   # One way to get to the first number [1, 9]
    for i in range(2, len(message)+1):
        ways_i = ways[i-1]
        char_2 = message[i-2:i]
        if int(char_2) >= 1 and int(char_2) <= 26:
            ways_i += ways[i-2]
        ways.append(ways_i)
    return ways[len(message)]

message = '121'   # answer should be 3
result = count_decodings(message)
print(result)
message = '135'   # answer should be 2
result = count_decodings(message)
print(result)
message = '1234'   # answer should be 3
result = count_decodings(message)
print(result)