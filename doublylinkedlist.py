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
    def insertatLast(self,val):
        node=Node(val)
        if not self.head:
            self.head=node
        else:
            current=self.head
            while current.next :
                current=current.next
            current.next=node 
            node.prev=current
    def insertatPosition(self,val,position):
        new_node=Node(val)
        if position==0:
            self.insertatHead(val)
            return 
        current=self.head
        count=0
        while current and count<position-1:
            current=current.next
            count+=1
        if current is None:
            print("Position out of bounds")
            return
        new_node.next=current.next
        new_node.prev= current
        if current.next:
            current.next.prev=new_node
        current.next=new_node
    def traverse(self):
        count=0
        temp=self.head
        if not self.head:
            return 0
        else:
            while temp :
                count+=1
                temp=temp.next
            return count
    def delete_head(self):
        if not self.head:
            return 
        else:
            temp=self.head
            if temp.next is None:
                self.head=None
            else:   
                self.head=temp.next
                temp.next.prev=None
                temp.next=None
    def deleteAtLast(self):
        if not self.head:
            return
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            if temp.prev is None:
                self.head=None
            else:
                temp.prev.next=None
                temp.prev=None
    def deleteInBetween(self,position):
        if not self.head:
            return
        else:
            temp=self.head
            if position==0:
                self.delete_head()
                return 
            count=0
            while temp.next and count<position-1:
                temp=temp.next
                count+=1
            if temp.next is None:
                return 
            if temp.next.next is None:
                node_to_delete = temp.next
                temp.next = None
                node_to_delete.prev = None
            else:
                
                node_to_delete = temp.next
                temp.next = temp.next.next
                temp.next.prev = temp
                node_to_delete.next = None
                node_to_delete.prev = None
           

            
                