#The Fibonacci Number Algorithm using Recursion


prev0 = 0
prev1 = 1
c=2

def fibo (prev0 , prev1):
    global c
    if c<=19:
        fib = prev0 + prev1
        print (fib)

        prev0 = prev1
        prev1 = fib
        c+=1
        fibo (prev0 , prev1)
    else:
        return