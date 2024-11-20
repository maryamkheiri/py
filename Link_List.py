class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class Link_list:
    def __init__(self,head):
        self.head=head
    def b_append(self,value):
        new_node=Node(value)
        new_node.next=self.head
        self.head=new_node
        
    def e_append(self,value):
        new_node=Node(value)
        temp=self.head
        while temp.next:
            temp=temp.next
        else:
            temp.next=new_node
    def __str__(self):
        _str=""
        temp=self.head
        while temp.next:
            _str+=str(temp.value)+"-->"
            temp=temp.next
        else:
            _str+=str(temp.value)
        return _str
    def __len__(self):
        length=0
        temp=self.head
        while temp.next:
            temp=temp.next
            length+=1
        else:
            temp=temp.next
            length+=1
        return length
    
    def add(self,value,index=None):
        if not index or index>len(self):
            self.e_append(value)
        elif index <0:
            self.b_append(value)
        else:
            new_node=Node(value)
            temp=pre=self.head
            #temp=temp.next
            index-=1
            while index>0:
                pre=temp
                temp=temp.next
                index-=1
            else:
                new_node=Node(value)
                new_node.next=temp
                pre.next=new_node

first=Node(5)
ml=Link_list(first)
print(ml)
ml.b_append("marry")
print(ml)
ml.e_append([1,2,3,4,"m"])
print(ml)
ml.add(6,2)
print(ml)
len(ml)
ml.add(3,-1)
print(ml)
ml.add(7,3)
print(ml)
len(ml)
