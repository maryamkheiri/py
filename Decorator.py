import time
def timer_decorator(original_func):
    def wrapper_function(*arg,**kwarg):
        start=time.time()
        result=original_func(*arg,**kwarg)
        time.sleep(0.003)
        end=time.time()
        print(f"your {original_func.__name__!r} took:{end-start:.4f} sec")
        return result
    return wrapper_function
@timer_decorator
def my_func(n):
    lst=sum(range(n))
    return lst
print(my_func(5000))