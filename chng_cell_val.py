from random import randint as rnd
def func(lst,n):
    length=len(lst)
    for i in range(length):
        _rnd=rnd(0,length-1)
        for j in range(n):
            new_cell=rnd(0,n-1)
            new_val=rnd(0,n-1)
            lst[_rnd][new_cell]=new_val
    return lst
lst=[[rnd(0,6) for j in range(0,6)]for i in range(0,6)]
print(lst)
current_lst=func(lst,6)
print(current_lst)