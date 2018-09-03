"""
Invert a binary tree.

For example, given the following tree:
    a
   / \
  b   c
 / \  /
d   e f

should become:
  a
 / \
 c  b
 \  / \
  f e  d
"""

# ---------------------------------------------------------
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_binary_tree(root):
    if root is None:
        return None
    new_right = invert_binary_tree(root.right)
    new_left = invert_binary_tree(root.left)
    root.left = new_right
    root.right = new_left
    return root

def print_binary_tree_helper(root, num_spaces):
    if root is None: return
    num_spaces += 2
    print_binary_tree_helper(root.right, num_spaces)
    print(' '*num_spaces + str(root.val))
    print_binary_tree_helper(root.left, num_spaces)

def print_binary_tree(root):
    print_binary_tree_helper(root, 0)

# ---------------------------------------------------------
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print('before:')
print_binary_tree(root)
print()
invert_binary_tree(root)
print('after:')
print_binary_tree(root)
print()

