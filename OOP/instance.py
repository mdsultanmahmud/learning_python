'''
Now we are learning about instance of python 
'''

class Employee:
    # now declare a class variables 
    companyName = "Tech-Hunt ORG"
    def __init__(self, name):
        self.name = name 
        # now declare a isinstance variables 
        self.salary_range = "20k-50k"
    def showDetails(self):
        print(f"The name of the employee is {self.name} in the company {self.companyName}. His salary range is {self.salary_range}")

e1 = Employee("Sultan")
e1.salary_range = "10k-20k" # i can change the value of this variables. so it is an isntance variables 
e1.showDetails()
e2 = Employee("Rahul")
e2.companyName = "Apple"
e2.showDetails()