class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None

class DoublyLinkedList:
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
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length+=1
        return True
    
    def pop(self):
        temp=self.tail
        if self.length==0:
            return None
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            self.tail=self.tail.prev
            self.tail.next=None
            temp.prev=None
        self.length-=1
        return temp.value
    
    def prepend(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
        self.length+=1
        return True
    
    def popfirst(self):
        if self.length==0:
            return None
        temp=self.head
        if self.length==1:
            self.head=None
            self.tail=None
        else:
           self.head=self.head.next
           self.head.prev=None
           temp.next=None
        self.length-=1
        return temp.value
    
    def get(self,index):
        if index<0 or index>=self.length:
            return None
        temp=self.head
        if index<self.length/2:
            for _ in range(index):
                temp=temp.next
        else:
            temp=self.tail
            for _ in range(self.length-1,index,-1):
                temp=temp.prev
        return temp

    def set_value(self,index,value):
        temp=self.get(index)
        if temp:
            temp.value=value
            return True
        return False
    
    def insert(self,index,value):
        if index<0 or index>self.length:
            return False
        if index==0:
            return self.prepend(value)
        if index==self.length:
            return self.append(value)
        
        new_node=Node(value)
        before=self.get(index-1)
        after=before.next

        new_node.prev = before
        new_node.next=after
        before.next=new_node
        after.prev=new_node

        self.length+=1
        return True
    
    def remove(self,index):
        if index<0 or index>=self.length:
            return None
        if index == 0:
            return self.popfirst()
        if index==self.length-1:
            return self.pop()
        
        temp=self.get(index)
        # temp.next.prev=temp.prev
        temp.prev.next=temp.next
        temp.prev=None
        temp.next=None

        # temp=self.get(index)

        # before=temp.prev
        # after=temp.next

        # temp.next=None
        # temp.prev=None
        # before.next=after
        # after.prev=before

        self.length-=1
        return temp.value
    
my_DLL = DoublyLinkedList(4)
my_DLL.append(66)
my_DLL.append(6)
my_DLL.append(5)
my_DLL.prepend(99)

my_DLL.set_value(1,18)

my_DLL.insert(2,23456)



my_DLL.print_list()




#POP node 
# print(my_DLL.pop())
# print(my_DLL.pop())
# print(my_DLL.pop())

#pop first
print("----------------------------------------------------")
# print(my_DLL.popfirst())
# print(my_DLL.popfirst())
# print(my_DLL.popfirst())
# print(my_DLL.popfirst())

#get
# print(my_DLL.get(3))

#remove

print(my_DLL.remove(1))


