import heapq
class Heapqueue:
    def __init__(self):
        #self.data=data
        self.children=[]
    def push(self,value,priority):
        heapq.heappush(self.children,(-priority,value))
    def pop(self):
        if len(self.children)==0:
            raise IndexError("out of index")
        else:
            val=heapq.heappop(self.children)
            return val[-1]
        

my_ququq=Heapqueue()
my_ququq.push(5,3)
my_ququq.push(6,2)
my_ququq.push(1,4)
my_ququq.push(10,5)
print(my_ququq.children)
print(my_ququq.pop())
print(my_ququq.pop())
print(my_ququq.pop())
print(my_ququq.pop())
print(my_ququq.children)

