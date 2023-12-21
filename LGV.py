x = 20 #global variable

def printSomething():
    x = 10 #local variable
    global y 
    y = 5
    print(f"The value of x is(local): {x}")
    print("Hello")

printSomething()
print(f"The value of x is(global): {x}")

print(y)

