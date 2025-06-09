'''You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.'''

class Node:
    def __init__(self, data):
        self.data = data        # Store node value
        self.next = None        # Pointer to next node

class LinkedList:
    def __init__(self):
        self.start = None       # Head of the linked list
    
    def insert_at_end(self, data):
        new_node = Node(data)   # Create new node with given data
        if self.start is None:  # If list is empty, new node is head
            self.start = new_node
            return
        last_node = self.start
        while last_node.next:   # Traverse to last node
            last_node = last_node.next
        last_node.next = new_node  # Append new node at end

    def print_linked_list(self, head):
        current = head
        while current:          # Traverse the list from given head
            print(f"{current.data}---> ", end='')  # Print current node value
            current = current.next
        print("None")           # Indicate end of list

    def mergeTwoLists(self, list1, list2):
        # NOTE: change Node to ListNode and data to val to run on LeetCode
        dummy = Node(-1)       # Create dummy node as starting anchor
        tail = dummy           # Tail pointer to build merged list
        ptr1 = list1           # Pointer for first list
        ptr2 = list2           # Pointer for second list
        
        while ptr1 and ptr2:   # Traverse both lists while both have nodes
            if ptr1.data < ptr2.data:
                tail.next = ptr1    # Append smaller node to merged list
                ptr1 = ptr1.next    # Move pointer in first list
            else:
                tail.next = ptr2
                ptr2 = ptr2.next    # Move pointer in second list
            tail = tail.next        # Move tail to last node in merged list

        # Attach remaining nodes from list that is not exhausted
        if ptr1:
            tail.next = ptr1
        if ptr2:
            tail.next = ptr2

        return dummy.next            # Return head of merged list (skip dummy)

# ----------------- Testing -----------------

l1 = LinkedList()
l2 = LinkedList()
list1 = [1,2,4]
list2 = [1,3,4]

# Build linked lists from arrays
for v in list1:
    l1.insert_at_end(v)
for v in list2:
    l2.insert_at_end(v)

s1 = l1.start    # Head of first linked list
s2 = l2.start    # Head of second linked list
print(l1.print_linked_list(s1))    # Print first list
print(l2.print_linked_list(s2))    # Print second list

merged = l1.mergeTwoLists(s1, s2)  # Merge two sorted lists
l1.print_linked_list(merged)        # Print merged list
