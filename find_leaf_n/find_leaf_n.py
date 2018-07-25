"""
Given a binary tree, find the Nth leaf node.
"""

# -----------------------------------
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_leaf_n_helper(root, leaves):
    if root.left is None and root.right is None:
        leaves.append(root.val)
        return leaves
    leaves = find_leaf_n_helper(root.left, leaves)
    leaves = find_leaf_n_helper(root.right, leaves)
    return leaves

def find_leaf_n(root, n):
    leaves = []
    leaves = find_leaf_n_helper(root, leaves)
    print(leaves)
    return leaves[n-1]

# -----------------------------------
# Leaves: [4, 5, 6, 7]
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

result = find_leaf_n(root, 3)
print(result)
