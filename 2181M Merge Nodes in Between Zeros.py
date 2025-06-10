'''
# TODO
You are given the head of a linked list, which contains a series of integers separated by 0's. The beginning and end of the linked list will have Node.val == 0.

For every two consecutive 0's, merge all the nodes lying in between them into a single node whose value is the sum of all the merged nodes. The modified list should not contain any 0's.

Return the head of the modified linked list.
'''

# FIXME change Node to ListNode, data to val, self.start to head to run on Leetcode

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
    
    def mergeNodes(self, head):
        new_list = Node(-1)                     # create a dummy node
        current = new_list                      # save starting address of the dummy node
        slow = fast = self.start                # initialise 2 pointers to keep track of starting and ending zeroes
        c = 0                                   # initialise a counter
        while fast:                             # loop till fast is None
            c += fast.data                      # keep adding data at current nodes address
            if fast.data == 0 and slow != fast: # if current nodes data is 0 and slow and fast are different which means slow is at starting zero and fast is at ending zero
                current.next = Node(c)          # create another node in a new list with data c and store its address in current nodes pointer
                current = current.next          # update current to point at the new node
                c = 0                           # reset counter to 0        
                slow = fast                     # update slow to point at current 0 which will be starting 0 for upcoming numbers
            fast = fast.next                    # update fast to visit other nodes
        return new_list.next                    # skip first dummy node and return 2nd node from where the new list starts
        
# ----------------- Testing -----------------

ll1 = LinkedList()
head = [0,3,1,0,4,5,2,0]

# Build linked list
for v in head:
    ll1.insert_at_end(v)

ll1.print_linked_list()
x = ll1.mergeNodes(head)
ll1.print_linked_list(x)