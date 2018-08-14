"""
Given the root to a binary search tree, find the second largest node in the tree.
"""

# ----------------------------------------
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bst_insert(root, val):
    if root is None:
        return Node(val)
    if val < root.val:
        root.left = bst_insert(root.left, val)
    elif val > root.val:
        root.right = bst_insert(root.right, val)
    return root

def bst_second_largest_1(root):
    if root is None:
        return
    print(root.val, end=", ")
    bst_second_largest_1(root.left)
    bst_second_largest_1(root.right)

# ----------------------------------------
root = Node(5)
root = bst_insert(root, 3)
root = bst_insert(root, 2)
root = bst_insert(root, 4)
root = bst_insert(root, 7)
root = bst_insert(root, 6)
root = bst_insert(root, 8)

bst_second_largest_1(root)