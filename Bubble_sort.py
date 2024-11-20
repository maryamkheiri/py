from random import randint as rnd
import matplotlib.pyplot as plt

length=10
_list=[rnd(0,length) for i in range(length)]
print(_list)
for i in range(length-1):
    flag=True
    for j in range(length-i-1):
        if _list[j]>_list[j+1]:
            flag=False
            _list[j],_list[j+1]=_list[j+1],_list[j]
        plt.bar(list(range(length)),_list)
        plt.pause(0.06)
        plt.clf()
    if flag:
        break
plt.bar(list(range(length)),_list)
plt.show()
print(_list)