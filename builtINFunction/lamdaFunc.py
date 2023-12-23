# def square(x):
#     return x * x 

# now using lambda function create same things 
square = lambda x: x * x 
cube = lambda x: x*x*x
avg = lambda x,y,z: (x + y + z) / 3
# print(avg(3,4,5))
# print(avg(4,6,78))
# print(square(5))
# print(cube(5))

def appl(fx, value):
    return 6 + fx(value)

print(appl(lambda x: x * x * x, 2))