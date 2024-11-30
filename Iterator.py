class Customiter:
    def __init__(self,start=0,limit=None,step=1):
        self.start=start
        self.limit=limit
        self.step=step
        self.__iter__()
    def __iter__(self):
        self.value=self.start
        return self
    def __next__(self):
        x=self.value
        if  self.limit  is not None:
            if self.value<self.limit:
                self.value+=self.step
            else:
                raise StopIteration         
        else:
            self.value+=self.step    
        return x
myiter=Customiter(1,10,2)
for i in myiter:
    print(i)
lst=[1,2,3,4,5,6]
class My_iter:
    def __init__(self,obj):
        self.obj=obj
        self.__iter__()
    def __iter__(self):
        self.index=0
        return self
    def __next__(self):
        try:
            x=self.obj[self.index]
            self.index+=1
        except:
            raise StopIteration
        return x
my_iter=My_iter("Python3")
for i in my_iter:
    print(i)