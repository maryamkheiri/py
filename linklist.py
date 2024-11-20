class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Link_list:
    def __init__(self):
        self.head=None
        self.length=0
    def push(self,val):
        new_node=Node(val)
        new_node.next=self.head
        self.head=new_node
        self.length+=1
    def __repr__(self):
        _str=""
        temp=self.head
        while temp.next:
            _str+=str(temp.data) + "->"
            temp=temp.next
        else:
            _str+=str(temp.data)
        return _str
    def __len__(self):
        return self.length
    def isempty(self):
        return self.length==0
    def append(self,val):
        temp=self.head
        while temp.next:
            temp=temp.next
        else:
            new_node=Node(val)
            temp.next=new_node
            self.length+=1
    def insert(self,index,val):
        if index<=0:
            self.push(val)
        elif index>=self.length:
            self.append(val)
        else:
            temp=self.head
            index-=1
            while index:
                temp=temp.next
                index-=1
            else:
                new_node=Node(val)
                new_node.next=temp.next
                temp.next=new_node
                self.length+=1
    def pop(self,index=-1):
        if index<0:
            temp=self.head
            while temp.next.next:
                temp=temp.next
            else:
                _data=temp.next.data
                temp.next=None
                self.length-=1
                return _data
        elif index==0:
            _data=self.head.data
            self.head=self.head.next
            self.length-=1
            return _data
        else:
            temp=self.head
            index-=1
            while index:
                temp=temp.next
                index-=1
            else:
                _data=temp.next.data
                temp.next=temp.next.next
                self.length-=1
                return _data
    def setter(self,lst):
        for i in lst[::-1]:
            self.push(i)

    def reverse(self):
        pre=None
        cur=_next=self.head
        while cur:
            _next=cur.next
            cur.next=pre
            pre=cur
            cur=_next
        else:
            self.head=pre
    def hasloop(self):
        if self.head:
            slow=fast=self.head
            while slow and fast and fast.next:
                slow=slow.next
                fast=fast.next.next
                if slow == fast:
                    return True
            else:
                return False
ll=Link_list()
ll.setter([1,2,3,4,5,66])
print(ll)
print(ll.hasloop())