
# age  = 28
# if(age >= 18 and age <= 24):
#     print("You are perfect for marry but you should late!!")
# elif (age > 24):
#     print("You are perfect for marray!!!")
# else: 
#     print("You are not perfect for driving!")

# num = 20 
# num = 60
# if(num == 20 or num > 50):
#     print(("wow its:{0}".format(num)))

'''
shor hand if else as like as ternary operator in js
'''
# try: 
#     age = int(input("Enter your age in integer number: "))
#     if age > 18:
#         print("You are perfect for marriege!!")
#     else: 
#         print("You are not perfect for marriege!!")
# except Exception as e:
#     print("Please enter valid integer number!!")

try: 
    a = 25 
    b = 200
    print("A") if a > b else print("B")
    c = a if a > b else b
    print("The greater number is: ", c)
    # print("A") if  a>b else print("=") if a == b else print("B")
except Exception as e:
    print("Error", e)
