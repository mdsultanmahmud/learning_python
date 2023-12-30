# class Employee:
#     def __init__(self, name, id,salary):
#         self.name  = name 
#         self.id = id 
#         self.salary = salary
#     def showDetails(self):
#         print(f"Details about {self.name}:\n I 'm {self.name}. My id is {self.id} and my salary is {self.salary}\n\n")


# # inheritance 
# class Programmer(Employee):
#     def progrmmer(self):
#         print("The default programming language is Python!")


# e1 = Employee("Md. Sultan Mahmud", "0001", 30500)
# e2 = Employee("Md. Rahul Islam", "0002", 50000)
# e3 = Employee("Md. Kabir Khan", "0003", 20000)
# e4 = Programmer("Mst. Nilima Akter", "0004", 15000)
# e1.showDetails()
# e2.showDetails()
# e3.showDetails()
# e4.showDetails()
# e4.progrmmer()


class Student:
    def __init__(self, name,age):
        self.name  = name 
        self.age = age
    def show(self):
        print(f"My name is {self.name} and i'm in {self.age} years old!!")

class Profession(Student ):
    def __init__(self,name, age, prof):
        super().__init__(name, age)
        self.prof = prof 
    def profession(self):
        print(f"I'm working as {self.prof}")

s1 = Student("Sultan", 20 )
s2 = Profession("Rahul Islam", 25,"Programmer")
s2.show()
s2.profession()
# s1.show()
