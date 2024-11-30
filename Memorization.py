from functools import lru_cache,cache
def factorial(n):
    if n==0 or n==1:
        return 1
    return n* factorial(n-1)
def factorial1(n,cache={}):
    if n in cache:
         return cache[n]
    if n ==0 or n==1:
        cache[n]=1
    else:
        cache[n]=n*factorial1(n-1,cache)
    return cache[n]
@lru_cache
def factorial2(n):
    if n==0 or n==1:
        return 1
    return n* factorial2(n-1)
@cache
def factorial3(n):
    if n==0 or n==1:
        return 1
    return n* factorial3(n-1)
