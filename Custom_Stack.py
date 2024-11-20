from collections import deque
import logging
logging.basicConfig(level=logging.WARNING , format="%(levelname)s:%(msg)s - %(name)s")
class Cstack:
    def __init__(self):
        self.container=deque()
    def push(self,val):
        self.container.append(val)
    def pop(self):
        try:
            return self.container.pop()
        except:
            logging.warning("Stack is Empty")
    def peek(self):
        try:
            return self.container[-1]
        except:
            logging.warning("Stack is Empty")
    def __len__(self):
        return len(self.container)
    def isempty(self):
        if len(self.container):
            return False
        else:
            return True
    def __repr__(self):
        return f"{self.container}"
    
mystack=Cstack()
mystack.push(5)
mystack.push(4)
mystack.push(9)
print(mystack)
print(mystack.isempty())
print(mystack.peek())
print(len(mystack))
mystack.pop()
mystack.pop()
mystack.pop()
mystack.pop()
print(mystack.isempty())