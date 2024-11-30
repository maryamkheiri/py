import threading,thread
from concurrent.futures import ThreadPoolExecutor
import time
a=10
mylock=threading.Lock()
lst_sample=[]
def my_func(x):
    global a
    with mylock:
        b=a
        b+=x
        time.sleep(1)
        a=b
        print("value is:",a)
    
#print(threading.__file__)
def add_list(x):
    global lst_sample
    with mylock:
        for i in range(20):
            lst_sample.append(x)
    print(lst_sample)
if __name__=="__main__":
    th1=threading.Thread(target=my_func , args=(10,))
    th2=threading.Thread(target=my_func,args=(30,))
    th1.start()
    th2.start()
    th1.join()
    th2.join()
    print("final value is",a)
    th3=threading.Thread(target=add_list,args=(10,))
    th4=threading.Thread(target=add_list,args=(30,))
    th3.start()
    th4.start()
    th3.join()
    th4.join()
    print("total lst is:",lst_sample)
class my_thread:
    def __init__(self):
        self.lock=threading.Lock()
        self.queue=list()
    def append_queue(self,value):
        with self.lock:
            for _ in range(10):
                time.sleep(0.01)
                self.queue.append(value)
            print(self.queue)
    def run(self):
        th1=threading.Thread(target=self.append_queue, args=("a",))
        th2=threading.Thread(target=self.append_queue,args=("b",))
        th1.start()
        th2.start()
        th1.join()
        th2.join()
        
if __name__ == "__main__":
    my_obj=my_thread()
    my_obj.run()
lst=[]
lock=threading.Lock()
def count(n):
    global lst
    with lock:
        for _ in range(1,n+1):
            lst.append(_)
            time.sleep(1)
        print(lst)
            
start=time.time()
tasks=[]
num=[1,2,3,4,5,6]
for i in range(2):
    th=threading.Thread(target=count,args=(10,))
    th.start()
    tasks.append(th)
for task in tasks:
    task.join()
print(threading.active_count())
print("final",lst)
print("it took:",round(time.time()-start,2),"secons")