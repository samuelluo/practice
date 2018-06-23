# --------------------------------------------------
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# --------------------------------------------------
def serialize(node, array=[]):
    if node is None:
        array.append(None)
    else:
        array.append(node.val)
        serialize(node.left, array)
        serialize(node.right, array)
        return array

# --------------------------------------------------
# When converting from list to tree, pre-order is required.
# Must create the root Node first. Can't visit left before root exists.
def deserialize(array):
    val = array.pop(0)
    if val is None:
        return None
    else:
        root = Node(val)
        root.left = deserialize(array)
        root.right = deserialize(array)
        return root

# --------------------------------------------------
node = Node('root', Node('left', Node('left.left')), Node('right'))
array = serialize(node)
print(array)

node = deserialize(array)
array = serialize(node)
print(array)