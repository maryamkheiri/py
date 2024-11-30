import concurrent.futures
import time
nums=[1,2,3,4,5,6]
nums1=[]
def my_func(n):
    print(f"Going to sleep for:{n} secs")
    time.sleep(n)
    return f"Finished sleeping after:{n} secs"


def my_add_lst(n):
    global nums1
    nums1.append(n)
    return nums1
        
with concurrent.futures.ThreadPoolExecutor() as executer:
    tasks=[executer.submit(my_func,num)for num in nums]
    for task in concurrent.futures.as_completed(tasks):
        print(task.result())
print("Donnnn")
start=time.time()
with concurrent.futures.ThreadPoolExecutor() as executor:
    tasks=[executor.submit(my_add_lst,num)for num in nums]
    for task in concurrent.futures.as_completed(tasks):
        print(task.result())
print(f"it has taken:{round(time.time()-start,2)} secons.")