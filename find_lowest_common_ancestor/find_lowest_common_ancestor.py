# -----------------------------------
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_path(root, num):
    path = []
    find_path_helper(root, num, path)
    return path

def find_path_helper(root, num, path):
    if root is None: return False
    path.append(root.val)
    if root.val == num or \
       find_path_helper(root.left, num, path) or \
       find_path_helper(root.right, num, path):
        return True
    path.pop()
    return False

def lowest_common_ancestor(root, num_1, num_2):
    path_1 = find_path(root, num_1)
    path_2 = find_path(root, num_2)
    if len(path_1) == 0 or len(path_2) == 0:
        return None
    else:
        for i in range(min(len(path_1), len(path_2))):
            if path_1[i] != path_2[i]:
                return path_1[i-1]
        # If all nodes match, LCA is the last node in the path
        return path_1[min(len(path_1), len(path_2))-1]

# -----------------------------------
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
path = find_path(root, 4)
print(path)
result = lowest_common_ancestor(root, 4, 5)    # Answer: 2
print(result)
result = lowest_common_ancestor(root, 4, 6)    # Answer: 1
print(result)
result = lowest_common_ancestor(root, 3, 4)    # Answer: 1
print(result)
result = lowest_common_ancestor(root, 6, 3)    # Answer: 3
print(result)