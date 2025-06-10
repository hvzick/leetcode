'''
# TODO
Given the head of a linked list head, in which each node contains an integer value.

Between every pair of adjacent nodes, insert a new node with a value equal to the greatest common divisor of them.

Return the linked list after insertion.

The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

'''

# FIXME: Change self.start to head, data to val, to run on Leetcode

from typing import Optional
from math import gcd
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

    def print_linked_list(self, head=None):
        current = head if head else self.start
        while current:
            print(f"{current.data}---> ", end='')
            current = current.next
        print("None")
    
    def insertGreatestCommonDivisors(self, head):
        prev = self.start                          # initialise prev from 2st node
        current = prev.next                        # initialise current from 2nd node
        while current:                             # loop till current has data in it
            gcd_val = gcd(prev.data, current.data) # find gcd and store it
            temp = prev.next                       # store  value of next node in temop variable to prevent losing it when inserting a node
            new_node = Node(gcd_val)               # create a new node
            prev.next = new_node                   # store new node in previous nodes address pointer
            new_node.next = temp                   # store the temp variables data in new nodes address pointer
            prev = prev.next.next                  # change the prev node 2 times because we inserted a node so we do not want to calculate its gcd
            current = current.next                 # increment current nodes address
        return self.start                          # return starting address
        
# ----------------- Testing -----------------

ll1 = LinkedList()
head = [18,6,10,3]

# Build linked list
for v in head:
    ll1.insert_at_end(v)

ll1.print_linked_list()
ll1.insertGreatestCommonDivisors(head)
ll1.print_linked_list()