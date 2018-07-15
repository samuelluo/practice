"""
Suppose you start with the number 1 and can multiply by 2 or floor divide by 3.
Find the operations needed to reach a target number.
"""

target = 7
queue = [1]
operations = {1: []}
while len(queue) != 0:
    num = queue.pop(0)
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
        print('1', end='')
        for i in range(len(ops)):
            op = ops[i]
            if op == 2:
                print(' * 2', end='')
            if op == 3:
                print(' / 3', end='')
        print(' = ' + str(target))
        break
    queue.append(num*2)
    if num//3 != 0:
        queue.append(num//3)