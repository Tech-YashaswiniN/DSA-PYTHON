class Stack:
    def __init__(self):
        self.stack_list = []
    
    def print(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])
    
    def push(self,item):
        self.stack_list.append(item)

    def is_empty(self):
        return len(self.stack_list) == 0
    
    def pop(self):
        if not self.is_empty():
            return self.stack_list.pop()
    
    def peek(self):
        if not self.is_empty():
            return self.stack_list[-1]
    
    def size(self):
        return len(self.stack_list)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

stack.print()
print("---------------------")

print("Is empty: ",stack.is_empty())
print("Top element is: ",stack.peek())
print("The size of the stack of list is: ",stack.size())
print("The item poped is: ", stack.pop())