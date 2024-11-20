class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class CLod:
        def __init__(self):
            self.head=None
            self.length=0
        def push(self,value):
            new_node=Node(value)
            if self.head:
                temp=self.head
                while temp.next!=self.head:
                    temp=temp.next
                else:
                    new_node.next=self.head
                    self.head=new_node
                    temp.next=self.head
                    self.length+=1
            else:
                self.head=new_node
                new_node.next=self.head
                self.length=1
        def __repr__(self):
            _str=""
            if self.head:
                temp=self.head
                while temp.next!=self.head:
                    _str+=str(temp.value) + "->"
                    temp=temp.next
                else:
                    _str+=str(temp.value) + "->[Loop]"
            return _str
        def pop_fist(self):
            val=None
            if self.head:
                if self.length==1:
                    val=self.head.value
                    self.head.next=None
                    self.head=None
                    self.length=0
                    return val
                elif self.length>1:
                    val=self.head.value
                    temp=self.head
                    while temp.next!=self.head:
                        temp=temp.next
                    else:
                        temp.next=self.head.next
                        self.head=self.head.next
                        self.length-=1
                        return val
            return val

        def pop_mid(self,index=-1):
            val=None
            if self.head:
                if index==-1 or index>=self.length:
                    return self.pop_end()
                elif index<=0 or self.length==1:
                    return self.pop_fist()
                else:
                    index-=1
                    temp=self.head
                    while index:
                        temp=temp.next
                        index-=1
                    else:
                        val=temp.next.value
                        temp.next=temp.next.next
                        self.length-=1
                        return val
            return val            

        def pop_end(self):
            val=None
            if self.head:
                if self.length>1:
                    temp=self.head
                    while temp.next.next!=self.head:
                        temp=temp.next
                    else:
                        val=temp.next.value
                        temp.next=self.head
                        self.length-=1
                        return val
                elif self.length==1:
                    val=self.head.value
                    self.head.next=None
                    self.head=None
                    self.length=0
                    return val
            return val


        
                    
my_ll=CLod()
my_ll.push(1)
my_ll.push(2)
my_ll.push(3)
my_ll.push(4)
print(my_ll)
print(my_ll.pop_mid(0))
print(my_ll)
                   
    
                    





                