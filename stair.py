def fib(n): 
    if n <= 1: 
        return n 
    return fib(n-1) + fib(n-2)  
def countWays(b): 
    return fib(b + 1)
a=input()
b=int(a)
c= countWays(b)
print(c)
