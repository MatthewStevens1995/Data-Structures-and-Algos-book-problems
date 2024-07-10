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
    
    def add(self,item):
        """method that adds the next node to the linked list"""
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    
    def length(self)->int:
        """traverses the linked link and returns 
        the count of items in the unordered linked list"""
        current = self.head
        count = 0
        while current != None:
            count = count+1
            current = current.getNext()
        return count
    
    def search(self,itm):
        """function traverses the unordered linked list
        and returns True if the argument is found in the list"""
        current = self.head
        found = False
        while (current != None) and (not found):
            if current.getData() == itm:
                return True
            else:
                current = current.getNext()
            
        return found
    
    def remove(self,itm):
        """function that removes an item in the list
        based on the value inputted,assume its in the list"""
        current = self.head
        found = False
        previous = None
        while not found:
            if current.getData()==itm:
                found=True
            else:
                previous = current
                current=current.getNext()
        if previous==None:
            self.head=current.getNext()
        else:
            previous.setNext(current.getNext())
            
    def append(self,item):
          """method that appends an item to the end of the list"""
          new_node = Node(item)
          if self.head is None:
            self.head = new_node
          else:
            current = self.head
            while current.getNext() is not None:
                current = current.getNext()
            current.setNext(new_node)
            
    def insert(self,pos,item):
        """method to insert node at any position in the list"""
        new_node = Node(item)
        index = 0
        current = self.head
        previous = None
        #find the index where the insertion needs to be
        while index< pos:
            index = index+1
            previous = current
            current = current.getNext()
        #once index==position, execute insertion logic
        previous.setNext(new_node)
        new_node.setNext(current)
    
    def index(self,item):
        """function that returns the index an item is at in an unordered list"""
        current = self.head
        index = 0
        while current.getData() != item:
            index = index+1
            current= current.getNext()
        return index
    
    def pop(self):
        """removes the last node item from the list, returns the removed nodes data"""
        current = self.head
        previous = None
        while current.getNext() is not None:
            previous = current
            current=current.getNext()
        previous.setNext(None)
        return current.getData()
        
class OrderedList:
    def __init__(self) -> None:
        """init method which implements class attributes"""
        self.head = None
        
    def IsEmpty(self)->bool:
        """Returns true if the list is empty, otherwise false"""
        return self.head == None
    
    def Length(self)->int:
        """Returns the count of items in the list"""
        current = self.head
        count = 0
        while self.head is not None:
            count = count +1
            current = current.getNext()
        return count
    
    def Remove(self,item:any)->None:
        """Removes the item argument, returns None, assume its in the list"""
        current = self.head
        found = False
        previous = None
        while not found:
            if current.getData()==item:
                found=True
            else:
                previous = current
                current=current.getNext()
        if previous==None:
            self.head=current.getNext()
        else:
            previous.setNext(current.getNext())
            
    def search(self,item:int)->bool:
        """searches for the inputted value, returns true if its in the list,
        false if its not in the list"""
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData()== item:
                found = True
            else:
                if current.getData()>item:
                    stop = True
                else:
                    current = current.getNext()
        return found