from random import randint as rnd
amount=10
_list=[rnd(1,amount) for i in range(amount)]
print(_list)
new_lst=[]
for i in _list:
    for j in range(len(new_lst)):
        if i<new_lst[j]:
            new_lst.insert(j,i)
            break
    else:
        new_lst.append(i)
print(new_lst)
for i in range(1,amount):
    for j in range(i):
        if _list[j]>_list[i]:
            item=_list[i]
            _list.pop(i)
            _list.insert(j,item)
print(_list)
        