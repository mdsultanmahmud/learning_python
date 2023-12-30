class MyClass: 
    def __init__(self, value ) :
        self._value = value 
    def show(self):
        print(f"Value is {self._value}")
    @property
    def value(self):
        return self._value 

obj1  = MyClass(20)   
obj1._value = 100 
print(obj1._value) #object is not callable
obj1.show()