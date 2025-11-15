class Node:
    def __init__(self, data):
        self.data=data
        self.next=None


class CircularLinkedList:
    def __init__(self):
        self.head=None

    def insert_end(self, data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            new_node.next=self.head
            return
        current=self.head
        while current.next!=self.head:
            current=current.next
        current.next=new_node
        new_node.next=self.head

    def print_list(self):
        if self.head is None:
            print("List is empty")
            return
        current=self.head
        while True:
            print(current.data, end=" -> ")
            current=current.next
            if current==self.head:
                break
        print("(back to head)")

cll=CircularLinkedList()
cll.insert_end(10)
cll.insert_end(20)
cll.insert_end(30)
cll.print_list()