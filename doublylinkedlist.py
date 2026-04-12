class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None
class DoublyLinkedList:
    def __init__(self):
        self.head=None
    # insert at head
    def insertatHead(self,val):
        node1=Node(val)
        if not self.head:
            self.head=node1
        else:
            node1.next=self.head
            self.head.prev=node1
            self.head=node1
