


#----------------------Linear Data Structures:----------------------------------------------

class Stack:
    """A Stack is a Linear data structure. Its like a list in that it accepts heterogenough elements.
    Its defined by its 'first in,last out' property in that elements can only be added and removed to the stack
    from the same side. thus older elements are removed before newer elements added"""
    def __init__(self):
        self.item = []
        
    def isEmpty(self):
        return len(self.item) == 0
    
    def push(self,item):
        self.item.append(item)
    
    def peek(self):
        return self.item[-1]
    
    def size(self):
        return len(self.item)
    
    def pop(self):
        return self.item.pop()
    
