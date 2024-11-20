class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None
class CQueue:
    def __init__(self):
        self.head=None
        self.front=None
    def enqueue(self,value):
        new_node=Node(value)
        if self.head==None:
            self.head=new_node
            self.front=new_node
        else:
            self.front.next=new_node
            new_node.prev=self.front
            self.front=new_node
    def __repr__(self):
        _str=""
        if self.head:
            temp=self.head
            while temp.next:
                _str+=str(temp.value) + "<->"
                temp=temp.next
            else:
                _str+=str(temp.value)
        return _str
    
my_queue=CQueue()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
print(my_queue)
print(my_queue.head.next.next.value)