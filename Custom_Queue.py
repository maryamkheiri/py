from collections import deque
import logging
logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler=logging.FileHandler("log.log")
streamer=logging.StreamHandler()
formater=logging.Formatter("%(levelname)s:%(name)s:%(message)s")
file_handler.setFormatter(formater)
streamer.setFormatter(formater)
logger.addHandler(file_handler)
logger.addHandler(streamer)

class Cqueue:
    def __init__(self):
        self.container=deque()
    def enqueue(self,val):
        self.container.appendleft(val)
    def dequeue(self):
        try:
            return self.container.pop()
        except:
            logger.error("Queue is Empty")
    def peek(self):
        try:
            return self.container[-1]
        except:
            logger.debug("Queue is Empty")
    def isempty(self):
        if len(self.container):
            return False
        else:
            return True
    def __len__(self):
        return len(self.container)
    def __repr__(self):
        return f"{self.container}"

myqueue=Cqueue()
myqueue.enqueue(4)
myqueue.enqueue(7)
myqueue.enqueue(8)
myqueue.enqueue(0)
print(myqueue)
print(myqueue.isempty())
print(myqueue.peek())
print(len(myqueue))
print(myqueue.dequeue())
print(myqueue.dequeue())
print(myqueue.dequeue())
print(myqueue.dequeue())
myqueue.dequeue()
myqueue.peek()
