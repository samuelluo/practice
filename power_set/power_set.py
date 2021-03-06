"""
The power set of a set is the set of all its subsets. Write a function that,
given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return
{{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.
"""

# ---------------------------------------------------------
def power_set(elements):
    elements = list(elements)
    power_set = []
    for i in range(2**len(elements)):
        binary = bin(i)[2:]
        binary = '0'*(len(elements)-len(binary)) + binary
        power_set_i = []
        power_set_i = [elements[i] for i in range(len(binary)) if binary[i] == '1']
        # print([binary, power_set_i])
        power_set.append(power_set_i)
    return power_set

# ---------------------------------------------------------
elements = set([1,2,3])
result = power_set(elements)
print(result)
print()

elements = set(['A', 'A', 'B', 'C', 'D'])
result = power_set(elements)
print(result)
print()