'''
# TODO
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.'''

# FIXME Change Node to ListNode and data to val to run on Leetcode and only copy paste the function defnition not function heading

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

    
    def addTwoNumbers(self, l1, l2):
        dummy = Node(-1)
        new_node = dummy
        ptr1 = l1
        ptr2 = l2
        carry = 0
        while ptr1 or ptr2 or carry:             # Loop till no node and carry number is left
            val1 = ptr1.data if ptr1 else 0      # check if ptr1 exists 
            val2 = ptr2.data if ptr2 else 0      # if not store 0
            total = val1 + val2 + carry          # calculate total
            carry = total // 10                  #ccalculate carry
            current_digit = total % 10           # calculate current digit to put in the LinkedList
            new_node.next = Node(current_digit)  # create new node with current digit as data
            new_node = new_node.next             # move the pointer to point to current node
            if ptr1:                             # if ptr1 exits
                ptr1 = ptr1.next                 # then move the pointer to next node
            if ptr2:                             # if ptr2 exists
                ptr2 = ptr2.next                 # then move the pointer to next node
        return dummy.next                        # return addres of 2nd node because first one is dummy and contains -1

# ----------------- Testing -----------------

ll1 = LinkedList()
ll2 = LinkedList()
l1 = [2,4,3]
l2 = [5,6,4]

# Build linked list
for v in l1:
    ll1.insert_at_end(v)
for v in l2:
    ll2.insert_at_end(v)
    
s1 = ll1.start
s2 = ll2.start
ll1.print_linked_list()
ll2.print_linked_list()
d = ll1.addTwoNumbers(s1, s2)
ll1.print_linked_list(d)