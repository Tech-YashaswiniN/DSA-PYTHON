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
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1
        return True

    
    #Find the middle node in the list
    def find_middle_node(self):
        slow=self.head
        fast=self.head

        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
        return slow

linkedlist=LinkedList(1)
linkedlist.append(2)
linkedlist.append(3)
linkedlist.append(4)
linkedlist.append(5)
linkedlist.print_list()
print("------------------------------------------------")
print("Middle Node is: ",linkedlist.find_middle_node().value)