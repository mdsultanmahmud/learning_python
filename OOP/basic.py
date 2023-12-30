'''
1. procedural programming (which we do basically)
2. object oriented programming


'''

#class and objects in python
 
class Person: 
    name = "Sultan"
    age = 20
    occupation = "Student"
    institue = "University of Rajshahi"
    def infoOfthePerson(myself):
        print(f"{myself.name} is a {myself.occupation}")
       


person1  = Person()
person1.name = "Rahul Islam"
person1.occupation = "Job Holder"
# print(person1.name) 
# print(person1.occupation)
person1.infoOfthePerson()
