from random import shuffle
import matplotlib.pyplot as plt

lenght=10
_list=[i for i in range(lenght)]
shuffle(_list)
print(_list)
for i in range(1,lenght):
    for j in range(i):
        if _list[i]<_list[j]:
            temp=_list[i]
            del _list[i]
            _list.insert(j,temp)
            break
    plt.bar(range(lenght),_list)
    plt.pause(0.05)
    plt.clf()
plt.bar(range(lenght),_list)
plt.show()
print(_list)