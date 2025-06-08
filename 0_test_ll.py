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
        print('None')

    def linearSearch(self, target):
        current = self.start
        n = 1
        while current:
            if current.data == target:
                print(f'Data found at {n}th node')
                return
            current = current.next
            n += 1
        print('Data not present in the Linked List')

    def insertAfter(self, prev, data):
        new_node = Node(data)
        current = self.start
        while current:
            if current.data == prev:
                temp = current.next
                current.next = new_node
                new_node.next = temp
                return
            current = current.next

    def reverse(self):
        prev = None
        current = self.start
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        self.start = prev



myLL = LinkedList()
myLL.insert_at_beginning(1)
myLL.insert_at_end(2)
myLL.insert_at_end(3)
myLL.insert_at_end(4)
myLL.insert_at_end(5)
myLL.linearSearch(3)
myLL.insertAfter(1, 11)    
myLL.print_linked_list()
myLL.reverse()
myLL.print_linked_list()

