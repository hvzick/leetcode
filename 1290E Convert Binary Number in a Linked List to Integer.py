'''Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

The most significant bit is at the head of the linked list.'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head) -> int:
        s = ''
        currentNode = head
        while currentNode:                      # loop till current node is not empty
            s += str(currentNode.val)           # convert value from int to str and store it
            currentNode = currentNode.next      # update current node with next node
        return int(s, 2)                        # Convert binary string to decimal

# Helper function to convert a list to a linked list
def list_to_linked_list(lst):
    if not lst:                         # Check if the input list is empty
        return None                     # Return None if there's nothing to convert
    head = ListNode(lst[0])             # Create the first node (head) from the first element
    current = head                      # Initialize a pointer to traverse and build the linked list
    for val in lst[1:]:                 # Loop through the rest of the list elements
        current.next = ListNode(val)    # Create a new node and link it to the current node
        current = current.next          # Move to the new node
    return head                         # Return the head of the newly created linked list

mySol = Solution()
head = list_to_linked_list([1, 0, 1])  # Convert list to linked list
print(mySol.getDecimalValue(head))