marks = [23,34,56,78,35,67,23,45,77,1,25]

# index = 0
# for mark in marks:
#     print(mark)
#     if(index == 3):
#         print("Hello programmers")
#     index +=1 

# same things using enumerate funciton 

for index, mark in enumerate(marks):
    print(mark, index)
    if(index == 3):
        print("Hello programmers") 