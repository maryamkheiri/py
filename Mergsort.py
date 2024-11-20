from random import shuffle
def combine(lst1,lst2):
    length1=len(lst1)
    length2=len(lst2)
    i=j=0
    lst=[]
    while i<length1 and j<length2:
        if lst1[i]<lst2[j]:
            lst.append(lst1[i])
            i+=1
        else:
            lst.append(lst2[j])
            j+=1
    lst+=lst1[i:]
    lst+=lst2[j:]
    return lst
def merg_sort(lst):
    if len(lst)==1:
        return lst
    else:
        mid=len(lst)//2
        left=lst[:mid]
        right=lst[mid:]
    left=merg_sort(left)
    right=merg_sort(right)
    return combine(left,right)
lst=[7, 11, 7, 9, 15, 1, 5, 0, 10, 5, 14, 3]
shuffle(lst)
print(lst)
print(merg_sort(lst))