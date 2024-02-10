class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None
        
class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
        
doubly_linked_list=DoublyLinkedList()
print(doubly_linked_list)