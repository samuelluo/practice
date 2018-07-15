"""
Suppose you start with the number 1 and can multiply (*) by 2 or divide (//) by 3.
Find the operations that would reach a target number.
"""

target = 7
queue = [1]
operations = {1: []}
while len(queue) != 0:
    num = queue.pop(0)
    print(num)
    print(queue)
    if num % 2 == 0 and num//2 in operations.keys():
        operations[num] = operations[num//2] + [2]
    elif num*3+0 in operations.keys():
        operations[num] = operations[num*3+0] + [3]
    elif num*3+1 in operations.keys():
        operations[num] = operations[num*3+1] + [3]
    elif num*3+2 in operations.keys():
        operations[num] = operations[num*3+2] + [3]
    if num == target:
        ops = operations[num]
        for i in range(len(ops)):
            print(i, end=' ')
            if i == 2:
                print('*', end=' ')
        print(operations[num])
        break
    queue.append(num*2)
    if num//3 != 0:
        queue.append(num//3)