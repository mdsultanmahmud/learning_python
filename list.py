marks = [2,3,4,56,25]
# print(marks)
# print(marks[0])
# print(marks[1])
# print(marks[2])

# for i in marks:
#     print(i)

# print(len(marks))

# list is mutable 

mixList = ["Sultan", 23, "Rahul", 10]
# for ele in mixList:
#     print(ele)

# print(mixList[-2])
# len(mixList) - 2

# if 23 in mixList:
#     print("Yes")
# else:
#     print("No")


# if "tan" in "Sultan":
#     print("Yes")
# else:
#     print("No")

# print(mixList[:])

def getPos(listOftheNum):
    for num in listOftheNum:
        if(num < 0):
            num = abs(num)
    return listOftheNum

# print(getPos([23,34,-58, -8, -9]))
# list comprehension 

# lst = [i for i in range(0, 5)]
# print(lst)
lst = [i for i in range(10) if i % 2 == 0]
# print(lst)

# list method 
l = [1,9,11,13, 2,3,4,6, 1, 1,1]
print(l)
# l.append(10)
# l.sort()
# l.sort(reverse=True)
# l.reverse()
# print(l.index(13))
# print(l.count(1))
# m = l # don't do that , main list will be change
# m = l.copy()
# m[0] = 0 
# l.insert(0, 100)
m = [500,600, 1000]
# l.extend(m)
k = l + m
# print(k)
# print(l)

