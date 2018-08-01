# Build list of sorted sum of cubes
cubes = [i**3 for i in range(1, 1000)]
soc_list = []    # [(soc, num_i, num_j)]
for j in range(len(cubes)):
    for i in range(j+1):
        num_i, num_j = cubes[i], cubes[j]
        soc = num_i + num_j
        soc_list.append((soc, num_i, num_j))
soc_list = sorted(soc_list, key=lambda x: x)

# Find which pairs sum up to the same SOC
soc_dict = {}    # {soc : [pairs]}
tcn_dict = {}    # {num_ways : tcn}
for soc, num_i, num_j in soc_list:
    if soc not in soc_dict.keys():
        soc_dict[soc] = []
    soc_dict[soc].append((num_i, num_j))
    num_ways = len(soc_dict[soc])
    if num_ways not in tcn_dict.keys():
        tcn_dict[num_ways] = {soc : soc_dict[soc]}

"""
{
    1: {2: [(1, 1)]},
    2: {1729: [(1, 1728),
               (729, 1000)]},
    3: {87539319: [(4657463, 82881856),
                   (11852352, 75686967),
                   (16581375, 70957944)]}
}
"""
print(tcn_dict)