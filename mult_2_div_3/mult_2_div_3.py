"""
Suppose you start with the number 1 and can multiply (*) by 2 or divide (//) by 3.
Find the operations that would reach a target number.
"""

target = 7
queue = [1]
operations = []
while len(queue) != 0:
    num = queue.pop(0)
    if num == target:
        print('target found')
        break
    queue.append(num*2)
    if num//2 != 0:
        queue.append(num//3)