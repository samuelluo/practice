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
    largest = second_largest = None
    queue = [root]
    while len(queue) != 0:
        node = queue.pop(0)
        if largest is None or node.val > largest:
            second_largest = largest
            largest = node.val
        elif second_largest is None or node.val > second_largest:
            second_largest = node.val
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return [largest, second_largest]

def bst_second_largest_2(root):
    """ For a BST, in-order traversal will pass through the nodes in
        increasing order. """
    bst_second_largest_2_helper(root, 0)

def bst_second_largest_2_helper(root, count):
    if root is None: return count
    count = bst_second_largest_2_helper(root.right, count)
    count += 1
    if count == 2:
        print("Second largest: {}".format(root.val))
    count = bst_second_largest_2_helper(root.left, count)
    return count

# ----------------------------------------
root = Node(5)
root = bst_insert(root, 3)
root = bst_insert(root, 2)
root = bst_insert(root, 4)
root = bst_insert(root, 7)
root = bst_insert(root, 6)
root = bst_insert(root, 8)
result = bst_second_largest_1(root)
print(result)
bst_second_largest_2(root)
print()

root = Node(1)
root = bst_insert(root, 2)
root = bst_insert(root, 3)
root = bst_insert(root, 4)
root = bst_insert(root, 5)
result = bst_second_largest_1(root)
print(result)
bst_second_largest_2(root)
print()
