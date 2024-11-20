lst=[0,4,2,3,7,8,9]
def linear_search(lst,k):
    for i in lst:
        if k==i:
            return "Found"
            break
    else:
            return "Not Found"
    
print(linear_search(lst,10))  
print(linear_search(lst,9))    