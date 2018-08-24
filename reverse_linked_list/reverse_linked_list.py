"""
Given the head of a singly linked list, reverse it in-place.
"""

# ---------------------------------------------------------
class Node:
    def __init__(self, val, next_=None):
        self.val = val
        self.next_ = next_

def build_linked_list(vals):
    head = Node(vals[0])
    curr_ = head.next_
    prev_ = head
    for val in vals[1:]:
        curr_ = Node(val)
        prev_.next_ = curr_
        prev_ = curr_
        curr_ = curr_.next_
    return head

def print_linked_list(head):
    print("[", end="")
    while head is not None:
        print(head.val, end="")
        head = head.next_
        if head is not None:
            print(", ", end="")
    print("]")

def reverse_linked_list(head):
    prev_ = None
    curr_ = head
    next_ = None
    while curr_ is not None:
        next_ = curr_.next_    # move next
        curr_.next_ = prev_    # reverse curr
        prev_ = curr_          # move prev
        curr_ = next_          # move curr
    head = prev_
    return head

# ---------------------------------------------------------
vals = [1,2,3,4]
head = build_linked_list(vals)
print_linked_list(head)
head = reverse_linked_list(head)
print_linked_list(head)
head = reverse_linked_list(head)
print_linked_list(head)
print()

vals = [1]
head = build_linked_list(vals)
print_linked_list(head)
head = reverse_linked_list(head)
print_linked_list(head)
print()
