class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next

    def append(self,value):
        new_node=Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length==0:
            return None
        
        temp=self.head
        pre=self.head
        while(temp.next):
            pre=temp
            temp=temp.next
        self.tail = pre
        self.tail.next=None
        self.length-=1

        if self.length==0:
            self.head=None
            self.tail=None
        return temp.value
    
    def prepend(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
            self.length+=1
        return True

    def pop_first(self):
        if self.length==0:
            return None
        temp=self.head
        self.head=self.head.next
        temp.next=None
        self.length-=1
        if self.length==0:
            self.tail=None
        return temp.value
    
    def get(self,index):
        if index<0 or index>=self.length:
            return None
        temp=self.head
        for _ in range(index):
            temp=temp.next
        return temp
    
    def set_value(self,index,value):
        temp=self.get(index)
        if temp:
            temp.value=value
            return True
        return False
    
    def insert_value(self,index,value):
        if index<0 or index>=self.length:
            return False
        if index==0:
            return self.prepend(value)
        if index==self.length:
            return self.append(value)
        new_node=Node(value)
        temp=self.get(index-1)
        new_node.next=temp.next
        temp.next=new_node
        self.length+=1
        return True
    
    def remove(self,index):
        if index<0 or index>self.length:
            return None
        if index==0:
            return self.pop_first()
        if index==self.length-1:
            return self.pop()
        prev=self.get(index-1)
        temp=prev.next
        prev.next=temp.next
        temp.next=None
        self.length-=1
        return temp.value
    
    def reverse(self):
        temp=self.head
        self.head=self.tail
        self.tail=temp
        after=temp.next
        before=None
        for _ in range(self.length):
            after=temp.next
            temp.next=before
            before=temp
            temp=after





my_linked_list=LinkedList(1)
my_linked_list.append(2)
my_linked_list.prepend(7)
# print("index 0 ",my_linked_list.get(0))
# print("index 1 ",my_linked_list.get(1))
# print("index 2 ",my_linked_list.get(2))
# my_linked_list.set_value(1,10)
my_linked_list.insert_value(1,989)
# print("The element was removed:",my_linked_list.remove(2),"\n")
my_linked_list.reverse()
my_linked_list.print_list()

# print(my_linked_list.pop_first())
# print(my_linked_list.pop_first())
# print(my_linked_list.pop_first())
# print(my_linked_list.pop_first())



# print(my_linked_list.pop())
# print(my_linked_list.pop())
# print(my_linked_list.pop())



# print("Head:", my_linked_list.head.value)
# print("Tail:",my_linked_list.tail.value)
# print("Length:",my_linked_list.length)
