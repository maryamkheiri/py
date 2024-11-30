def square(x):
    return x*x
def qube(x):
    return x*x*x
def my_map(my_func,my_list):
    result=[]
    for num in my_list:
        result.append(my_func(num))
    return result
print(my_map(square,[1,2,3,4,5,6]))
print(my_map(qube,[1,2,3,4,5,6]))
def outer_func(msg):
    def iner_func():
        print(msg)
    return iner_func
my_func=outer_func("hello")
print(my_func())
print(id(my_func))
print(id(outer_func))