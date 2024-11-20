 # the problem is  Implement hash table where collisions are handled using linear probing. 
#We learnt about linear probing in the video tutorial. Take the hash table implementation that uses chaining 
#and modify methods to use **linear probing**. Keep MAX size of arr in hashtable as 10.

class Hash_Table:#Implement hash table collision handling using linear probing
    def __init__(self):
        self.Max=10
        self.arr=[None for _ in range(self.Max)]
    def __getitem__(self,key):
        h=self.get_hach(key)
        if self.arr[h] is None:
            return 
        prob_index=self.prob_index(h)
        for _index in prob_index:
            elements=self.arr[_index]
            if elements is None:
                return 
            if elements[0]==key:
                return elements[1]

        
    def __setitem__(self,key,val):
        h=self.get_hach(key)
        if self.arr[h] is None:
            self.arr[h]=(key,val)
        else:
            new_index=self.find_slot(key,h)
            self.arr[new_index]=(key,val)
        print(self.arr)
                
    def get_hach(self,key):
        h=0
        for char in key:
            h+=ord(char)
        return h%self.Max
    def prob_index(self,index):
        return [*range(index,len(self.arr))]+[*range(0,index)]
    def find_slot(self,key,index):
        prob_index=self.prob_index(index)
        for _index in prob_index:
            if self.arr[_index] is None:
                return _index
            if self.arr[_index][0]==key:
                return _index
        raise Exception ("Hash Map is Full")

    def __delitem__(self, key):
        h=self.get_hach(key)
        prob_index=self.prob_index(h)
        for _index in prob_index:
            if self.arr[_index] is None:
                return # item not found so return. You can also throw exception
            if self.arr[_index][0]==key:
                self.arr[_index]=None
        print(self.arr)
t=Hash_Table()
print(t.arr)
t["march 6"] = 20
t["march 17"] =  88
t["march 17"] = 29
t["nov 1"] = 1
print(t["dec 1"])
t["march 33"] = 234
print(t["march 33"])
print(t["march 6"])
t["march 33"] = 999
print(t["march 33"])
t["april 1"]=87
t["april 2"]=123
t["april 3"]=234234
t["april 4"]=91
t["May 22"]=4
t["Jan 1"]=0
t["Jan 2"]=0
del t["Jan 1"]
t["Jan 2"]=0
del t["Jan 2"]






    