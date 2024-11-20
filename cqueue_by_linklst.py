from winotify import Notification,audio
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class CQueue:
    def __init__(self):
        self .head=None
        self.front=None
        self.length=0
    def enqeue(self,value):
        new_node=Node(value)
        if self.head:
            self.front.next=new_node
            self.front=self.front.next
        else:
            self.head=new_node
            self.front=new_node
        self.length+=1
    def dequeue(self):
        val=None
        if self.head:
            val=self.head.value
            self.head=self.head.next
            self.length-=1
        else:
            my_noty=Notification(
            app_id="my_app",
            title="Pop_Queue",
            duration="long",
            msg="CQueue is Empty",
            icon=r"C:\Users\USER\Desktop\py_projects\25- windows notification\icon.jpg")
            my_noty.set_audio(audio.LoopingAlarm9,loop=True)
            my_noty.show()
        return val
    def __repr__(self):
        _str=""
        if self.head:
            temp=self.head
            while temp.next:
                _str+=str(temp.value) +"->"
                temp=temp.next
            else:
                _str+=str(temp.value)
        else:
            my_noty=Notification(
                app_id="my_app",
                title="Print_Queue",
                duration="long",
                msg="CQueue is Empty",
                icon=r"C:\Users\USER\Desktop\py_projects\25- windows notification\icon.jpg")
            my_noty.set_audio(audio.LoopingAlarm9,loop=True)
            my_noty.show()
        return _str

my_queue=CQueue()
my_queue.enqeue(1)
my_queue.enqeue(2)
my_queue.enqeue(3)
my_queue.enqeue(4)
my_queue.enqeue(5)
print(my_queue)
print(my_queue.dequeue())
print(my_queue)