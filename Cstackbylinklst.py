from winotify import Notification,audio
class Node:
    def __init__(self,value):
        self.next=None
        self.value=value

class CStack:
    def __init__(self):
        self.head=None
        self.length=0
    def push(self,value):
        new_node=Node(value)
        if self.head:
            new_node.next=self.head
            self.head=new_node
        else:
            self.head=new_node
        self.length+=1
    def pop(self):
        val=None
        if self.head:
            val=self.head.value
            self.head=self.head.next
            self.length-=1
        else:
            my_note=Notification(
                app_id="my_app",
                title="MyTitle",
                duration="long",
                msg="CStack is Empty",
                icon=r"C:\Users\USER\Desktop\py_projects\25- windows notification\icon.jpg")
            my_note.set_audio(audio.LoopingCall, loop=True)      
            my_note.show()
        return val   
    def __repr__(self):
        _str=""
        if self.head:
            temp=self.head
            while temp.next:
                _str+=str(temp.value) + "->"
                temp=temp.next
            else:
                _str+=str(temp.value)
        return _str
    def __len__(self):
        return self.length
my_stack=CStack()
print(my_stack)
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
print(my_stack)
print(my_stack.pop())
print(my_stack)