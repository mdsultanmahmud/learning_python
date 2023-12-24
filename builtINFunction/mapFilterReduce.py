'''
we are learning map, filter and reduce method in python
'''

cube = lambda x: x * x * x
square = lambda x: x * x 
listOfNumber = [1,2,4,5,6,7,6,7,8]
# print(listOfNumber)
# using map method 
cubeOfList = list(map(cube, listOfNumber)) #we need to include a function and iterable items in map method 
squareOfList = list(map(square, listOfNumber)) #we need to include a function and iterable items in map method 
# print(f"Cube of the list: {cubeOfList}")
# print(f"Square of the list: {squareOfList}")


# using filter method 
filter_func = lambda x: x > 4
filter_func1 = lambda x: x < 6
filteredList = list(filter(filter_func, listOfNumber))
filteredList1 = list(filter(filter_func1, listOfNumber))
# print(f"Filtered list 1 (>4) is : {filteredList}")
# print(f"Filtered list 2 (6<) is : {filteredList1}")


# create a map function(higher order function )

def create_map(numbers, func):
    newList = []
    for i in range(len(numbers)):
        newNum = func(numbers[i])
        newList.append(newNum)
    return newList
# print(listOfNumber)
# print(create_map(listOfNumber, square))
# print(create_map(listOfNumber, cube))


# using reduce function 
from functools import reduce

sum = reduce(lambda x,y: x + y, listOfNumber)
print(sum)
# def summ(list):
#     sum = 0 
#     for i in range(len(list)):
#         sum += list[i]

#     return sum 

# print(summ(listOfNumber))

