# class LinkedList:
#     def __init__(self,val):
#         self.val=val
#         self.next=next

# node1=LinkedList(12)
# node2=LinkedList(14)
# node3=LinkedList(15)
# node1.next=node2
# node2.next=node3
        
# print(node1.next.next)
# print(node3)

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class SinglyLinkedList:
    def __init__(self):
        self.head=None
    def append(self,value):
        new_node=Node(value)
        if self.head==None:
            self.head=new_node
        else:
            current=self.head
            while current.next is not None:
                current=current.next
            current.next= new_node
    def traverse(self):
            if self.head==None:
                print("Linkedlist is empty")
            else:
                current=self.head 
                while current is not None:
                    print(current.value,end=" ")
                    current=current.next
sing=SinglyLinkedList()
sing.append(15)
sing.append(16)
sing.append(17)
sing.traverse()      
                    
                
            
            