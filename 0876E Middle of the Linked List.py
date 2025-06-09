'''# TODO
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.'''
from typing import Optional

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.start = None
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.start is None:
            self.start = new_node
            return
        last_node = self.start
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_linked_list(self):
        current = self.start
        while current:
            print(f"{current.data}---> ", end = '')
            current = current.next
        print("None")
    
    def middleNode(self, head):
        slow = head               # slow pointer moves one step at a time
        fast = head               # fast pointer moves two steps at a time
        while fast and fast.next:  # loop continues while there are nodes ahead for fast to jump
            slow = slow.next        # move slow one step
            fast = fast.next.next   # move fast two steps
        return slow               # when fast reaches end, slow is at the middle node


# ----------------- Testing -----------------

l1 = LinkedList()
head = [1,2,3,4,5,6]
n = 2

# Build linked list
for v in head:
    l1.insert_at_end(v)

s1 = l1.start
l1.print_linked_list()
l1.print_linked_list()
l1.print_linked_list()
mid_node = l1.middleNode(l1.start)
print("Middle Node is:", mid_node.data)