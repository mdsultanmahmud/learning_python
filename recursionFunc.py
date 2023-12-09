'''
recursion function: the function which call into the function
'''

def factorial(n):
    if(n == 0 or n == 1):
        return n
    return n * factorial(n  -1 )

# print(factorial(2))
# print(factorial(5))
# print(factorial(1))
# print(factorial(0))

# fibonacci series in python ==> 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89.... 

# def fib(n):
#      return fib(n - 1) + fib(n - 2)

# print(fib(3))