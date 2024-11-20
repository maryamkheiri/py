from random import shuffle
lst=[i for i in range(10)]
shuffle(lst)
print(lst)
def quick_sort(lst):
    lengh=len(lst)
    if lengh<=1:
        return lst
    pivot=lst.pop()
    left=[]
    right=[]
    for i in lst:
        if i<pivot:
            left.append(i)
        else:
            right.append(i)
    return quick_sort(left)+[pivot]+quick_sort(right)

print(quick_sort(lst))