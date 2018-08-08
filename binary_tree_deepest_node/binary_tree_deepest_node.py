"""
Given a binary tree, find the deep­est node in it.
"""

# ---------------------------------------------------------
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def deepest_node(root):
    queue = [(root, 0)]
    deepest = (root.val, 0)
    while len(queue) != 0:
        node, depth = queue.pop(0)
        if depth > deepest[1]:
            deepest = (node.val, depth)
        if node.left is not None:
            queue.append((node.left, depth+1))
        if node.right is not None:
            queue.append((node.right, depth+1))
    return deepest

# ---------------------------------------------------------
# Answer: (8, 3)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.right.right = Node(8)
result = deepest_node(root)
print(result)

# Answer: (6, 2)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(6)
result = deepest_node(root)
print(result)