from typing import Any


#----------------------Linear Data Structures:----------------------------------------------

class Stack:
    
    """A Stack is a Linear data structure. Its like a list in that it accepts heterogenough elements.
    Its defined by its 'first in,last out' property in that elements can only be added and removed to the stack
    from the same side. thus older elements are removed before newer elements added. its collections are ordered"""
    
    def __init__(self):
        """Initializes an empty Stack"""
        self.item = []
        
    def isEmpty(self)->bool:
        """Checks if the Stack is empty, returns a bool. If its empty returns true"""
        return len(self.item) == 0
    
    def push(self,item)->None:
        """Adds a item to the end of the Stack, returns none"""
        self.item.append(item)
    
    def peek(self)->Any:
        """Returns the item at the end of the Stack"""
        return self.item[-1]
    
    def size(self)->int:
        """Returns the count of of elements in the Stack"""
        return len(self.item)
    
    def pop(self)->Any:
        """Returns the last element in the Stack"""
        return self.item.pop()
    


class Queue:

    """A Queue is a like a Stack, except that The side of the list that removes/pops off elements and add elements are different sides.
    So instead of a Stack, which has a 'first in last out' property', A queue has a 'First in First out property. Queue elements can
    Be hetergenous. its collections are ordered"""
    
    def __init__(self):
        """Initialize an empty stack upon object instantiantion"""
        self.queue = []

    def enqueue(self,item)->None:
        """Adds an item to the start of the queue. method returns nothing"""
        self.queue.insert(0,item)
        
    def dequeue(self)->Any:
        """Pops off the item in at the back of the queue. Returns the item popped off"""
        return self.queue.pop()
    
    def isEmpty(self)->bool:
        """asks if the queue is empty. Returns a bool: True if its empty, False if not"""
        return self.queue == []
    
    def size(self)->int:
        """Returns the number of Items in the Queue"""
        return len(self.queue)
    
    
class Deque:
    
    """A Deque, pronouched 'deck' is a linear, ordered data structure.
    What makes It different than the other two linear Data Structures above
    is that items can be added and removed from either side of the data structure.
    so you can add items to be beginning, the end, and remove items from the beginning
    and end. items can be heterogenous like the other linear data structures."""
    
    def __init__(self):
        """initialize an empty Deque upon instiantion"""
        self.items = []

    def isEmpty(self)->bool:
        """checks if Deque is empty, returns bool"""
        return self.items == []
    
    def addFront(self,item)->None:
        """adds an item to the front,returns none"""
        self.items.append(item)
    
    def addRear(self,item)-> None:
        """adds an item to the rear, returns none"""
        self.items.insert(0,item)
    
    def removeFront(self)->Any:
        """removes an item from the front, returns the item"""
        return self.items.pop()
    
    def removeRear(self)->Any:
        """removes an item from the rear, returns the item """
        return self.items.pop(0)

    def size(self)->int:
        """Checks the numer of items in the deque, returns int"""
        return len(self.items)
    

class Node:
    
    """this is a Node class used to implement a Linked list"""
    
    def __init__(self, initdata):
        """initializes a node, holding a reference to what value/object it is,
        and that the next node its connected to is set to None by Default (relative position)"""
        self.data = initdata
        self.next = None
        
    def getData(self):
        """function that returns the object/reference the node contrains"""
        return self.data
    
    def getNext(self):
        """returns the next node that the current node is connected to (relative position)"""
        return self.next
    
    def setData(self,newdata):
        """function that overwrites the current nodes data its holding"""
        self.data = newdata
    
    def setNext(self,newnext):
        """function that overwrites what is the next node that this node points to in the
        relative position of the linked list."""
        self.next = newnext
        

class UnorderedList:
    """class to represent an unordered list.
    only data it has is telling the first node in the linked list"""
    
    def __init__(self):
        """a reference to the first node in the linked list"""
        self.head = None
    
    def isEmpty(self):
        """Simple boolean checking if the node reference attribute is none or not"""
        return self.head == None