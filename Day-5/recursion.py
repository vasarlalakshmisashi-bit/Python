#recursion
def fn1(n):
    if(n>=0):
        fn1(n-1)
        print(n)
fn1(5)
def fn1(n):
    if(n>0):
        fn1(n-1)
        print(n)
fn1(5)
def fn1(n):
    if(n>0):
        fn1(n-1)
        print(n,end=" ")
fn1(5)
#factorial of a number using recursion
def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))
