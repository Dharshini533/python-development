class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SinglyLinkedList:
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

    def print_list(self):
        current=self.head
        while current:
            print(current.data, end="->")
            current=current.next
        print("None")

x=SinglyLinkedList()
x.insert_end(12)
x.insert_end(2)
x.insert_end(1)
x.print_list()
