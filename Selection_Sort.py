from random import randint as rnd
amount=10
_list=[rnd(1,amount) for i in range(amount)]
print(_list)
for i in range(amount-1):
    _min=i
    for j in range(i,amount):
        if _list[j]<_list[_min]:
            _min=j
    _list[i],_list[_min]=_list[_min],_list[i]
print(_list)