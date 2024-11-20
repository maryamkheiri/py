lst=[]
with open(r"C:\Users\USER\Desktop\Practicing\data-structures-algorithms-python-master\data_structures\4_HashTable\stock_prices.csv","r") as f:
    for line in f:
        element=line.rstrip('\n').split(",")
        day=element[0]
        val=element[1]
        lst.append([day,val])
    print(lst)
class Hash:
    def __init__(self):
        self.max=10
        self.arr=[[] for _ in range(self.max)]
        
    def get_hash(self,key):
        h=0
        for char in key:
            h+=ord(char)
        return h%self.max
    def __setitem__(self,key,val):#handling collision by chaining techninqe
        h=self.get_hash(key)
        flag=False
        for idx,element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                self.arr[h][idx]=(key,val)
                flag=True
                break
        if not flag:
            self.arr[h].append((key,val))

    def __getitem__(self,key):
        h=self.get_hash(key)
        for element in self.arr[h]:
            if element[0]==key:
                return element[1]

    def __delitem__(self,key):
        h=self.get_hash(key)
        for idx,element in enumerate(self.arr[h]):
            if element[0]==key:
                del self.arr[h][idx]
print("TEst Cases:")
t=Hash()
t["march 6"] = 310
t["march 7"] = 420
t["march 8"] = 67
t["march 17"] = 63457
print(t.arr)
t["march 6"] = 31
print(t.arr)
t["march 6"]
t['march 17']
del t['march 17']
print(t.arr)

#problem figure out solution for below problems    
#1. What was the average temperature in first week of Jan
#2. What was the maximum temperature in first 10 days of Jan
dict={}
with open(r"C:\Users\USER\Desktop\Practicing\data-structures-algorithms-python-master\data_structures\4_HashTable_2_Collisions\Solution\nyc_weather.csv","r") as f:
    for line in f:
        elemnts=line.rstrip('\n').split(",")
        date=elemnts[0]
        temp=elemnts[1]
        try:
              dict[date]=int(temp)
        except:
              print("Invalid temperature.Ignore the row")
lst=[]
with open(r"C:\Users\USER\Desktop\Practicing\data-structures-algorithms-python-master\data_structures\4_HashTable_2_Collisions\Solution\nyc_weather.csv","r") as f:
    for line in f:
        elemnts=line.rstrip('\n').split(",")
        try:
             temp=int(elemnts[1])
             lst.append(temp)
        except:
              print("Invalid temperature.Ignore the row")

print("TEst Cases:")
print(dict)
dict['Jan 5']
dict['Jan 10']
print("average is:",sum(lst[0:7])/len(lst[0:7]))
print("maximum is:",max(lst[0:10]))

# the problem is You have to read this file (poem) in python and print every word and its count
text_dic={}
with open(r"C:\Users\USER\Desktop\Practicing\data-structures-algorithms-python-master\data_structures\4_HashTable_2_Collisions\Solution\poem.txt","r") as f:
       for line in f:
        elemnts=line.rstrip('\n').split(" ")
        for item in elemnts:
            if item in text_dic:
                text_dic[item]+=1
            else:
                text_dic[item]=1
print("Testcases:")
print(text_dic)






        