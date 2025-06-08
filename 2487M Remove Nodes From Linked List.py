'''You are given the head of a linked list.

Remove every node which has a node with a greater value anywhere to the right side of it.

Return the head of the modified linked list.'''

from typing import Optional

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.start = None
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.start
        self.start = new_node
    
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

    def removeNodes(self, head: Optional[Node]) -> Optional[Node]:
        # Reverse the linked list
        prev = None
        current = head
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        head = prev  # new head after reversal

        # Remove nodes with smaller values than previous
        prev = head
        current = head.next
        while current:
            if current.data < prev.data:
                # Skip current node
                prev.next = current.next
                current = current.next
            else:
                prev = current
                current = current.next

        # Reverse the list again to restore original order (with nodes removed)
        prev = None
        current = head
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        return prev  # new head of processed list


# ----------------- Testing -----------------

myLL = LinkedList()
values = [5, 2, 13, 3, 8]

# Build linked list
for v in values:
    myLL.insert_at_end(v)

print("Original List:")
myLL.print_linked_list()

# Call removeNodes
new_head = myLL.removeNodes(myLL.start)

# Update the start pointer to new head after removal
myLL.start = new_head

print("After removeNodes:")
myLL.print_linked_list()
