class MinHeap:
    def __init__(self,arr=None):
        self.heap=[]
        if type(arr) is list:
            self.heap=arr.copy()
        for i in range(len(self.heap))[::-1]:
            self._siftdown(i)
    def _siftup(self,i):
        parent=(i-1)//2
        while i!=0 and self.heap[i]<self.heap[parent]:
            self.heap[i],self.heap[parent]=self.heap[parent],self.heap[i]
            i=parent
            parent=(i-1)//2
    def _siftdown(self,i):
        left=2*i+1
        right=2*i+2
        while ((left<len(self.heap) and self.heap[left]<self.heap[i] ) or (right<len(self.heap) and self.heap[right]<self.heap[i])):
            smallest=left if (right>=len(self.heap) or self.heap[left]<self.heap[right]) else right
            self.heap[smallest],self.heap[i]=self.heap[i],self.heap[smallest]
            i=smallest
            left=2*i+1
            right=2*i+2
            
    def insert(self,element):
        self.heap.append(element)
        self._siftup(len(self.heap)-1)
        
    def get_min(self):
         return self.heap[0] if len(self.heap)!=0 else None

    def extract_min(self):
        if len(self.heap)==0:
            return None
        self.heap[0],self.heap[-1]=self.heap[-1],self.heap[0]
        minval=self.heap.pop()
        self._siftdown(0)
        return minval

    def update_by_index(self,i,new):
        old=self.heap[i]
        self.heap[i]=new
        if new<old:
            self._siftup(i)
        else:
            self._siftdown(i)

    def update(self,old,new):
        if old in self.heap:
            self.update_by_index(self.heap.index(old),new)

class Heapqueue: #priority-queue
    def __init__(self):
        self.queue=MinHeap()
    def enqueue(self,element):
        self.queue.insert(element)
    def peek(self):
        return self.queue.get_min()
    def dequeue(self):
        return self.queue.extract_min()
    def change_prioriy_by_index(self,i,new):
        self.queue.change_prioriy_by_index(i,new)
    def change_priority(self,old,new):
        self.queue.change_priority(old,new)
    def is_empty(self):
        return len(self.queue.heap)==0

heap=MinHeap([9,4,10,3,5])
print(heap.heap)
heap.insert(8)
heap.insert(2)
print(heap.heap)
print(heap.get_min())
print(heap.extract_min())
print(heap.heap)
heap.update_by_index(2,7)
print(heap.heap)
heap.update(9,6)
print(heap.heap)
my_queue=Heapqueue()
print(my_queue.is_empty())
my_queue.enqueue((0,9))
print(my_queue.queue.heap)
print(my_queue.is_empty())    