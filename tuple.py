
"""
# print("We are learning tupple in python")
# tuple is not mutable where list is mutable
tuple as like as list but not changable
"""
tup = (1,2,5,6,70)
# tup[0] = 15 #its not possible+
# print(type(tup), tup) 
# print(tup[0])

# if we want to change the tuple, first we need to convert tuple into a list then we can change 

friends = ("Omar", 'rahul', 'suruz','radit', 'faizur')
convertedTuple = list(friends)
convertedTuple.append("The last frnds")
convertedTuple.pop(3)
convertedTuple[0] = "Omar Faruk"
friends = tuple(convertedTuple)
# print(type(friends), friends)
