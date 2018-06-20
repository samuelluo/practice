class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ----------------------------------------
def is_unival(root):
    return is_unival_helper(root, root.val)

def is_unival_helper(root, value):
    if root is None:
        return True
    return root.val == value and \
           is_unival_helper(root.left, value) and \
           is_unival_helper(root.right, value)

# ----------------------------------------
def count_unival_trees(root):
    if root is None: return 0
    num_unival = 0
    num_unival += count_unival_trees(root.left)
    num_unival += count_unival_trees(root.right)
    if is_unival(root): num_unival += 1
    return num_unival

def count_unival_trees_2(root):
    num_unival, is_unival = count_unival_trees_2_helper(root)
    return num_unival

def count_unival_trees_2_helper(root):
    if root is None: return [0, True]
    num_unival = 0
    num_left, left_unival   = count_unival_trees_2_helper(root.left)
    num_right, right_unival = count_unival_trees_2_helper(root.right)
    num_unival = num_left + num_right
    if (left_unival and right_unival) and \
       (root.left is None or root.val == root.left.val) and \
       (root.right is None or root.val == root.right.val):
        return [num_unival + 1, True]
    else:
        return [num_unival, False]

# ----------------------------------------
root = Node('a',
            Node('a'),
            Node('a',
                 Node('a'),
                 Node('A')))
result = count_unival_trees(root)
print(result)
result = count_unival_trees_2(root)
print(result)

root = Node('a',
            Node('c'),
            Node('b',
                 Node('b'),
                 Node('b',
                      None,
                      Node('b'))))
result = count_unival_trees(root)
print(result)
result = count_unival_trees_2(root)
print(result)