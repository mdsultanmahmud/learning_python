'''
we are learning decorators!!

'''


def start(fx):
    def mfx(*args, **kwargs):
        print("Hello, This is our add function!!")
        fx(*args, **kwargs)
        print("Thanks for using this function!!!")
    return mfx


@start 
def add(a, b):
    print(a + b )


# add(10, 20)

def printSomething():
    print("Hello world!!")

# start(printSomething)()



def decorated(fx):
    def mfx(*args, **kwargs):
        print("Welcome to inside our decorated function")
        fx(*args, **kwargs)
        print("Thanks for using our decorated func!")
    return mfx 


@decorated
def callMe():
    print("Hi, i am inside of the decorated func!")

# callMe()

@decorated
def multiply(x,y):
    print(f"Multiplication of {x} and {y} is {x * y}")

# multiply(5,6)