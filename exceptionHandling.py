# '''
# we can handle error in python by using exception handling method
# as like as try(){}, catch() in js
# '''  

# num = input("Enter the number: ")
# print(f"Multiplicatiob table of {num} is: ")
# try: 
#     for i in range(1 , 11):
#         print(f"{i} * {num} = {i * int(num)}")
# except Exception as e:
#     print("Error: ", e)


# print("another lines of code!!")
# print("im running even throuh program is throwing error!")

# try:
#     num = int(input("Enter an integer number: "))
#     print("your number: ",num)
# except ValueError:
#     print("Invalid input, please input an integer number")
# finally:
#     print("It will always execute!")

# try:
#     num = int(input("Enter a integer: "))
#     a = [32,43,453,255]
#     print(a[num])
# except ValueError: 
#     print("Please input integer number")
# except IndexError:
#     print("Please input integer number 0 to 3")
# finally:
#     print("this is finally code block. im always execute!")

    # finally is neseccery for function 
def useTryExcept():
    try:
        num = int(input("Enter a integer: "))
        a = [32,43,453,255]
        print(a[num])
        return 1
    except ValueError: 
        print("Please input integer number")
        return 0
    except IndexError:
        print("Please input integer number 0 to 3")
        return 0
    finally:
        print("this is finally code block. im always execute!")

useTryExcept()

 