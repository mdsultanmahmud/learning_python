'''
its not necessary to use static method, just learn it. 
static function is a common function which initialize into the class with @staticmethod decorators and use as common function. 
'''

class Math:
    def __init__(self, num):
        self.num = num 
    def addToNum(self, n):
        self.num = self.num + n 
    @staticmethod 
    def add(a, b):
        return a + b 
    
a = Math(5)

print(a.num)
a.addToNum(20)
print(a.num)

print(a.add(25, 20)) # use static function 