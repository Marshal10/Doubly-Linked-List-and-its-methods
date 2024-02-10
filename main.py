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
        
    def __str__(self):
        temp=self.head
        result=''
        while temp:
            result+=str(temp.value)
            if temp.next:
                result+=" <-> "
            temp=temp.next
        return result
        
    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
        self.length+=1
        
    def prepend(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.head.prev=new_node
            new_node.next=self.head
            self.head=new_node
        self.length+=1
        
    def traverse(self):
        current=self.head
        while current:
            print(current.value)
            current=current.next
            
    def reverseTraverse(self):
        current=self.tail
        while current:
            print(current.value)
            current=current.prev
            
    def search(self,target):
        current=self.head
        index=0
        while current:
            if current.value==target:
                return index
            current=current.next
            index+=1
        return -1
    
    def get(self,index):
        if self.head is None or index < 0 or index >= self.length:
            return None
        if index <= self.length//2:
            current=self.head
            for _ in range(index):
                current=current.next
        else:
            current=self.tail
            for _ in range(self.length-1,index,-1):
                current=current.prev
        return current
    
    def set_value(self,index,value):
        update_node=self.get(index)
        if update_node:
            update_node.value=value
            return True
        return False
    
    def insert(self,index,value):
        new_node=Node(value)
        if index < 0 or index > self.length:
            print("Index out of bounds")
            return
        if index==0:
            self.prepend(value)
            return
        elif index==self.length:
            self.append(value)
            return
        temp_node=self.get(index-1)
        new_node.next=temp_node.next
        new_node.prev=temp_node
        temp_node.next.prev=new_node
        temp_node.next=new_node
        self.length+=1
        
doubly_linked_list=DoublyLinkedList()
doubly_linked_list.append(10)
doubly_linked_list.append(20)
# print(doubly_linked_list)
doubly_linked_list.prepend(5)
doubly_linked_list.prepend(15)
# doubly_linked_list.traverse()
# doubly_linked_list.reverseTraverse()
print(doubly_linked_list)
doubly_linked_list.insert(0,40)
print(doubly_linked_list)