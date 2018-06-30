def counting_sort_1(nums):
    counts = [0 for i in range(10)]
    for i in nums:
        counts[i] += 1
    
    output = []
    for i in range(len(counts)):
        for j in range(counts[i]):
            output.append(i)
    return output

def counting_sort_2(string):
    """ time complexity:
        iterate once to build counts
        iterate ascii 256 & pull out N chars one by one
        O(n) + O(k) ~= O(n)? """
    counts = [0 for i in range(256)]
    for i in string:    # O(n)
        counts[ord(i)] += 1
    
    output = []
    for i in range(len(counts)):   # iterate K, the range of input
        for j in range(counts[i]):
            output.append(chr(i))
    return ''.join(output)

nums = [1, 4, 1, 2, 7, 5, 2]
result = counting_sort_1(nums)
print(result)
string = "testing123"
result = counting_sort_2(string)
print(result)