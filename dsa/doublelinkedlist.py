class Node:
    def __init__(self, data):
        self.data=data
        self.prev=None
        self.next=None
class DoublyLinkedList:
    def __init__(self):
        self.head=None

    def insert_end(self, data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=new_node
        new_node.prev=current

    def print_list(self):
        current=self.head
        while current:
            print(current.data,end=" <-> ")
            current=current.next
        print("None")

dll = DoublyLinkedList()
dll.insert_end(10)
dll.insert_end(20)
dll.insert_end(30)
dll.print_list()