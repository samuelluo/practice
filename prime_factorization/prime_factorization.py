import math

def prime_factorization(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = int(n/2)
    for i in range(3, int(math.sqrt(n))+1, 2):
        while n % i == 0:
            factors.append(i)
            n = int(n/i)
    if n != 1:
        factors.append(n)
    return factors

n = 658
result = prime_factorization(n)
print(result)
n = 4
result = prime_factorization(n)
print(result)
n = 3
result = prime_factorization(n)
print(result)