'''
class Person:
    name = "Sultan"
    age = 20 
    occ = "Student"
    def info(self):
        print(f"{self.name} is a {self.occ}")

sultan = Person()
sultan.name = "Md. Sultan Mahmud"
sultan.age = 20 
sultan.occ = "Student"
sultan.info()         

'''

# we don't have write  lot of code. we can make this by constructor 

class Person:
    def __init__(self, n ,o, age):
        # print(self)
        self.name = n 
        self.occ = o 
        self.age = age
        print(f"{n} is a {o}.")

sultan = Person("Md. Sultan Mahmud", "Student", 20)
rahul = Person("Md. Rahul Islam", 'Web Developer', 22)
jamil = Person("Jamil Ahmed", 'Data Scientist', 28)
print(sultan.name, sultan.age, sultan.occ)
# print(sultan.name)
