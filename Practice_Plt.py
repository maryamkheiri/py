#draw (plot $ bar $ scatter $pie $donut )graphs in matplotlib
import matplotlib.pyplot as plt
from random import randint as rnd
x=list(range(50))
y=[rnd(-10,10) for i in range(50)]
z=[rnd(-5,10) for i in range(50)]
c=("red")
plt.figure(figsize=(20,5))
plt.title("Gas Prices\n-10,10",color="purple",fontsize = 22)
plt.xlabel("Time" ,color="purple")
plt.ylabel("Raised_Price" , color="purple")
plt.plot(x,y,color=c, label="Gas")
plt.plot(x,z,color="green", label="Oil")
plt.grid()
plt.legend(shadow=True)
plt.show()

print("######")
x=list(range(50))
y=[rnd(-10,10) for i in range(50)]
z=[rnd(-5,5) for i in range(50)]
c=["red","green"]
plt.figure(figsize=(20,5))
plt.title("---")
plt.bar(x,y,color=c,label="Gas Price")
plt.plot(x,z,color="yellow",label="Oil Prce")
plt.legend(shadow=True)
plt.show()

print("@@@@@@@@")
def choose_point(num,_min,_max):
    lines=[rnd(_min,_max) for i in range(num)]
    return lines
x=choose_point(50,-10,10)
y=choose_point(50,-6,3)
_x=choose_point(50,-8,9)
_x=choose_point(50,-1,10)
plt.title("Scatterr Graph\n",color="purple")
plt.scatter(x,y,c=choose_point(50,100,500),cmap="viridis",s=choose_point(50,100,150),edgecolors="black",linewidths=1.0,label="Oil Prices",alpha=0.7)#alpha for taransparany
plt.scatter(x,y,c=choose_point(50,0,20),marker="*",cmap="viridis",s=choose_point(50,30,50),label="Oil Prices",linewidths=2.0,alpha=0.7)#alpha for taransparany
cb=plt.colorbar()
cb.set_label("Car_Price")
plt.legend(shadow=True)
plt.show()

print("*********")
labels=["Python","C++","Go","Php","Java","Rust"]
vals=[30,20,30,14,20,18]
cls=["gold","yellowgreen","teal","salmon","plum","red"]
plt.pie(vals,labels=labels,colors=cls,startangle=90,autopct="%2.2f%%")
plt.show()

print("^^^^^^^^^")
vals=[10,10,10,10,10,10]
labels=["Python","C++","Go","Php","Java","Rust"]
cls=["gold","yellowgreen","teal","salmon","plum","red"]
plt.pie(vals,labels=labels,colors=cls,autopct="%2.0f%%",hatch=['//', '\\\\', '||', '--', '++', 'xx', 'oo', 'OO', '..', '**'])#hatch is setting for pattern
plt.pie([100],colors=["white"],radius=0.8)
plt.show()

print("$$$$$$$$$$")
vals=[60,50,40,30,10,9,8,7,6]
labels=["Python","C++","Go","Php","Java","Rust","","",""]
cls=["gold","yellowgreen","teal","salmon","plum","red","silver","navy","tan"]
plt.pie(vals,labels=labels,colors=cls,autopct="%2.0f%%",explode=[0,0,0,0.1,0.2,0.3,0.4,0.5,0.6])
plt.savefig("./new_pig.png")
plt.show()

print("$$$$$$$$$$$$")
import matplotlib.pyplot as plt
import numpy as np
company=['GOOGL','AMZN','MSFT','FB']
revenue=[90,136,89,27]
profit=[40,2,34,12]
xpos=np.arange(len(company))
plt.xticks(xpos,company)
plt.title("Us Stocks")
plt.ylabel("revenue")
plt.bar(xpos-0.15,revenue,width=0.3,label="company.revenue")
plt.bar(xpos+0.15,profit,width=0.3,label="company.profit")
plt.legend(shadow=True,fontsize=8)
plt.show()

print("&&&&&&&&&&&&")
plt.yticks(xpos,company)
plt.title("Us Stocks")
plt.xlabel("revenue")
plt.barh(xpos-0.15,revenue,label="company.revenue")
plt.barh(xpos+0.15,profit,label="company.profit")
plt.legend(shadow=True,fontsize=8)
plt.show()