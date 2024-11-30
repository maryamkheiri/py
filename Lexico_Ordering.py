def swap(_list, index1, index2):
    _list[index1], _list[index2] = _list[index2], _list[index1]
    return _list
items = [1,2,3,4]
print(items)
while True:
    #step 1
    largets_i = -1
    for i in range(len(items)-1):
        if items[i] < items[i+1]:
            largets_i = i
    if largets_i == -1:
        break

    #step 2
    largest_j = 0
    for j in range(len(items)):
        if items[largets_i] < items[j]:
            largest_j = j

    #step 3
    items = swap(items, largets_i, largest_j)

    #step 4
    left_half = items[:largets_i+1]
    right_half = items[largets_i+1:]
    right_half.reverse()
    items = left_half + right_half

    print(items)