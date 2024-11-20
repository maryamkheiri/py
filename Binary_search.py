_list=[1,3,5,7,9,10,16]
def binary_search(lst,k):
    if len(lst)<2:
        if lst[0]==k:
            return "Found"
        else:
            return "Not Found"
    mid=len(lst)//2
    if lst[mid]==k:
        return "Fond"
    elif lst[mid]>k:
        return binary_search(lst[:mid],k)
    else:
        return binary_search(lst[mid:],k)

print(binary_search(_list,10))