from DataStructures import Queue
import random


class LogicGate:
    
    def __init__(self,n):
        self.label = n
        self.output = None
    
    def getLabel(self):
        return self.label
    
    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output
    

class BinaryGate(LogicGate):
    
    def __init__(self, n):
        super().__init__(n)
    
        self.pinA = None
        self.pinB = None
        
    def getPinA(self):
        if self.pinA == None:
            return int(input("enter pin A input for gate "+ self.getLabel()))
        else:
            return self.pinA.getFrom().getOutput()
    
    def getpinB(self):
         if self.pinB == None:
            return int(input("enter pin B input for gate "+ self.getLabel()))
         else:
            return self.pinB.getFrom().getOutput()

class UnaryGate(LogicGate):
    
    def __init__(self, n):
        super().__init__(n)
        
        self.pin = None
    
    def getPin(self):
        return  int(input("enter pin input for gate "+ self.getLabel()))
    

class AndGate(BinaryGate):

    def __init__(self, n):
        super().__init__(n)
        
    def performGateLogic(self):
        
        a = self.getPinA()
        b = self.getpinB()
        if a==1 and b==1:
            return 1
        else:
            return 0 

class NandGate(AndGate):
    
    def __init__(self, n):
        super().__init__(n)
        
    def performGateLogic(self):
        if super().performGateLogic() ==1:
            return 0
        else:
            return 1
class XorGate(BinaryGate):
    
    def __init__(self, n):
        super().__init__(n)
    
    def performGateLogic(self):
        
        a = self.getPinA()
        b = self.getpinB()
        if a == 0 and b ==0:
            return 0
        elif a==1 and b ==0:
            return 1
        elif a==0 and b==1:
            return 1
        else:
            return 0
        
class NorGate(BinaryGate):
    
    def __init__(self, n):
        super().__init__(n)
    
    def performGateLogic(self):
        
        a = self.getPinA()
        b = self.getpinB()
        if a == 0 and b ==0:
            return 1
        elif a==1 and b ==0:
            return 0
        elif a==0 and b==1:
            return 0
        else:
            return 0
    
    
    

class connector:
    
    def __init__(self,fgate,tgate):
        self.fromgate = fgate
        self.togate = tgate
        
        tgate.setNextPin(self)
        
    def getFrom(self):
        return self.fromgate
    
    def getTo(self):
        return self.togate
    
    def setNextPin(self,source):
        if self.pinA == None:
            self.pinA = source
        
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                raise RuntimeError("error no empty pins")



class HalfAdder:
    
    def __init__(self):
        self.and_element = AndGate("AndGate")
        self.xor_element = XorGate("XorGate")
        

    def carry_element(self):
        return self.and_element.performGateLogic()
    
    def sum_element(self):
        return self.xor_element.performGateLogic()
    def run_half_adder(self):
        return "the outcome of the carry for this circuit is {}"\
            " and the outcome for the sum is {}".format(self.carry_element(),self.sum_element())

circuit = HalfAdder()
circuit.run_half_adder()


def gcd(m,n):
        while m%n != 0:
            oldm = m
            oldn = n
            
            m = oldn
            n = oldm%oldn
        return n

class fraction:
    def __init__(self,num,den):
        
       if isinstance(num,int)==False:
           raise RuntimeError("you didnt enter a int num")
       elif isinstance(den,int) == False:
           raise RuntimeError("you didnt enter a int den")
       else:
           pass
    
       if den<0:
           den = abs(den)
           num = -num
            
        
       common = gcd(num,den)
       self.num = num//common
       self.den = den//common
        
    def getNum(self):
        return self.num
    
    def getDen(self):
        return self.den
    
    def show(self):
        print(self.num,"/",self.den)
    
    def __str__(self):
        return str(self.num)+"/"+str(self.den)
    
    def __repr__(self):
        class_name = type(self).__name__
        return'{0}: numerator = {1}, denominator = {2}'.format(class_name,self.num,self.den)
    
    
    def __add__(self,otherfraction):
        newnum = self.num * otherfraction.den + \
            self.den * otherfraction.num
        
        newden = self.den * otherfraction.den
        
        common = gcd(newnum,newden)
        return fraction(newnum//common,newden//common)
    
    def __radd__(self,other):
        newnum = other.num * self.den + \
            other.den * self.num
        
        newden = other.den * self.den
        
        common = gcd(newnum,newden)
        return fraction(newnum//common,newden//common)
    
    
    def __iadd__(self,otherfraction):
        newnum = self.num * otherfraction.den + \
            self.den * otherfraction.num
        
        newden = self.den * otherfraction.den
        
        common = gcd(newnum,newden)
        self.num = newnum
        self.den = newden
        
        return self.__str__()
    
    def __sub__(self, otherfraction):
        newnum = self.num * otherfraction.den - self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)
        return fraction(newnum // common, newden // common)
    
    def __mul__(self,otherfraction):
        newnum = self.num * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum,newden)
        return fraction(newnum//common,newden//common)
    
    def __truediv__(self,otherfraction):
        newnum = self.num * otherfraction.den
        newden = self.den * otherfraction.num
        common = gcd(newnum,newden)
        return fraction(newnum//common,newden//common)
    
    def __gt__(self,otherfraction):
        if (self.num/self.den) > (otherfraction.num/otherfraction.den):
            return True
        else:
            return False
    
    def __ge__(self,otherfraction):
        if (self.num/self.den) >= (otherfraction.num/otherfraction.den):
            return True
        else:
            return False
    
    def __lt__(self,otherfraction):
        if (self.num/self.den) < (otherfraction.num/otherfraction.den):
            return True
        else:
            return False
    
    def __le__(self,otherfraction):
        if (self.num/self.den) < (otherfraction.num/otherfraction.den):
            return True
        else:
            return False
        
    def __ne__(self,otherfraction):
        if (self.num/self.den) != (otherfraction.num/otherfraction.den):
            return True
        else:
            return False
    
fra = fraction(2,-3)
fra1 = fraction(4,5)
print(fra.__sub__(fra1))
print(fra.__mul__(fra1))
print(fra.__truediv__(fra1))
print(fra.__lt__(fra1))
print(fra.__ge__(fra1))
print(fra.__iadd__(fra1))
fra.show()

print(fra.__str__())
print(fra.__repr__())


li = ['eat','ate','tea','haley','sock']
dick = {}
for item in li:
    sorted_item = "".join(sorted(item))
    if sorted_item in dick.keys():
        dick[sorted_item].append(item)
    else:
        dick[sorted_item] = [item]
print(dick.values())
        


class Stack:
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
    


def parChecker(st:str)-> bool:
        """function that checks if a str of parenthesis
        are balanced"""
        s=Stack()
        for item in st:
            if item == '(':
                s.push(item)
            else:
                    if s.isEmpty() or s.pop() != '(':
                        return False

        if s.isEmpty():
            return True
        else:
            return False           
        
        
def matcher(peak: str, pop_symbol: str) -> bool:
    opens = "([{"
    closed = ")]{"
    if peak in closed and pop_symbol in opens:
        return opens.index(pop_symbol) != closed.index(peak)
    else:
        return False  # Return False if invalid symbols are passed

        
def symbolChecker(st:str)-> bool:
        """function that checks if a str of symbols
        are balanced"""
        s=Stack()
        for item in st:
            if item in ['(','{','[']:
                s.push(item)
            else:
                    if s.isEmpty() or matcher(item,s.pop()):
                        return False

        if s.isEmpty():
            return True
        else:
            return False           
        

print(parChecker('()))'))
print(symbolChecker('([)]'))
print(s.isEmpty())


def Binary_converter(num:int)->int:
    """function that takes in a large int and converts
    it into its binary representation"""
    rememStack = Stack()
    while num > 0:
        remainder = num%2
        rememStack.push(remainder)
        num = num//2
    
    binary_str = ''
    while not rememStack.isEmpty():
        binary_str = binary_str + str(rememStack.pop())
    
    print(binary_str)
    

def hot_potato(namelist,num):
    """this is an exercise to simulate hot potato.
    The person at the end of the list has a hot potato.
    as the potato switches hands, the person goes from the
    end of the queue to the beginning"""
    structure = Queue()
    for name in namelist:
        structure.enqueue(name)
    while structure.size()>1:
        for i in range(num):
            structure.enqueue(structure.dequeue())
        structure.dequeue()
    print(structure.dequeue())
    
names = ['haley','goos','baby','love','matthew','bob']
hot_potato(names,7)



#-------------------from here we are simulating a printer, page 114---

class Printer:
    def __init__(self,ppm):
        self.pagerate = ppm
        self.currenTask = None
        self.timeRemaining = 0
        
    def tick(self):
        if self.currenTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <=0:
                self.currenTask = None
    
    def busy(self):
        if self.currenTask != None:
            return True
        else:
            return False
    
    def startNext(self,newtask):
        self.currenTask = newtask
        self.timeRemaining = newtask.getPages() * 60/self.pagerate
        
        
class Task:
    def __init__(self,time):
        self.timestamp = time
        self.pages = random.randrange(1,21)
    
    def getStamp(self):
        return self.timestamp
    
    def getPages(self):
        return self.pages
    
    def waitTime(self,currenttime):
        return currenttime - self.timestamp
    
def newPrintTask():
    """a helper function that is the probability of a printing task
    being requested in a given second"""
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False
    

def PrinterSimulation(numSeconds,PagesPerMinute):
    
    labprinter = Printer(PagesPerMinute)
    PrintQueue = Queue()
    waitingtimes = []
    
    for currentsecond in range(numSeconds):
        
        if newPrintTask():
            task = Task(currentsecond)
            PrintQueue.enqueue(task)
        
        if (not labprinter.busy()) and (not PrintQueue.isEmpty()):
            nextask = PrintQueue.dequeue()
            waitingtimes.append(nextask.waitTime(currentsecond))
            labprinter.startNext(nextask)
        
        labprinter.tick()
    
    avgwaittime = sum(waitingtimes)/len(waitingtimes)
    print('The Avg waiting times were: {}'.format(avgwaittime))

#----------------------printer simumlation end-----------------------

