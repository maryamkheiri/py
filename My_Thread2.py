import threading
import time
lock=threading.Lock()
class my_thread(threading.Thread):
    def __init__(self,threadId,name,count):
        threading.Thread.__init__(self)
        self.threadId=threadId
        self.name=name
        self.count=count
    def run(self):
        print("Starting...",self.name+"\n")
        with lock:
            print_time(self.name,1,self.count)
        print("Ending....",self.name+"\n")

class my_thread1(threading.Thread):
    def __init__(self,threadId,name,count):
        threading.Thread.__init__(self)
        self.threadId=threadId
        self.name=name
        self.count=count
    def run(self):
        print("Starting...",self.name+"\n")
        lock.acquire()
        lock.release()
        print_time(self.name,1,self.count)
        print("Ending....",self.name+"\n")        
        
            
        
def print_time(name,delay,count):
    while count:
       time.sleep(delay)
       print("%s:%s %s"%(name,time.ctime(time.time()),count)+"\n")
       count-=1
    
    

th1=my_thread(1,"paying",10)
th2=my_thread1(2,"Emailing",5)
th3=my_thread1(3,"Confirming",5)
th1.start()
th2.start()
th3.start()
th1.join()
th2.join()
th3.join()
print("Donnnnn")
