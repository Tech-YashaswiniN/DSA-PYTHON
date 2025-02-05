class Stack:
    def __init__(self):
        self.stack_list = []
    
    def push(self, item):
        self.stack_list.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.stack_list.pop()
    
    def is_empty(self):
        return len(self.stack_list) == 0
    

def reverse_string(string):
    stack = Stack()

    for char in string:
        stack.push(char)
    
    reversed_str  = " "
    while not stack.is_empty():
        reversed_str += stack.pop()
    
    return reversed_str

print(reverse_string("Hello"))
print(reverse_string("Stack"))