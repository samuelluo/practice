"""
Using a function rand7() that returns an integer from 1 to 7 (inclusive) with 
uniform probability, implement a function rand5() that returns an integer from
1 to 5 (inclusive).
Using a function rand5() that returns an integer from 1 to 5 (inclusive) with 
uniform probability, implement a function rand7() that returns an integer from 
1 to 7 (inclusive).
"""

import random

rand5 = lambda: random.randint(1, 5)
counts = [0 for i in range(10)]
for i in range(100000):
    counts[rand5()] += 1
ratios = [i/sum(counts) for i in counts]
print(ratios)


# rand5   = [1,  2,  3,  4,  5]
# rand5*5 = [5, 10, 15, 20, 25]
# rand5*5 + rand5 = [6, 7, ..., 25, 26]
# rand5*5 + rand5 - 5 = [1, 2, ..., 20, 21]
# (rand5*5 + rand5 - 5)%7 = [0, 1, 2, 3, 4, 5, 6]
# (rand5*5 + rand5 - 5)%7 + 1 = [1, 2, 3, 4, 5, 6, 7]
rand7 = lambda: (rand5()*5 + rand5() - 5)%7 + 1
counts = [0 for i in range(10)]
for i in range(100000):
    counts[rand7()] += 1
ratios = [i/sum(counts) for i in counts]
print(ratios)