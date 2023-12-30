'''
Access modifiers 
There are three types of acc. mod. 
1. Public acc. mod. 
2. Private acc. mod. 
3. Protected acc. mod.

as usual python code is public access modifiers. 

'''

# public acc. mod. 

class PublicAcc:
    def __init__(self):
        self.name = "Public Access Modifiers"

a = PublicAcc()
# print(a.name ) #i can print it 

class PrivateAcc:
    def __init__(self):
        self.__name = "Private Access Modifiers"
        self.__accessType = "You can be access indirectly!"
        # here __name for __ it is being private 
b = PrivateAcc()
# private acc. mod. (can not be accessed directly)
# print(b.__name)
# but can be accessed indirectly 
# print(b._PrivateAcc__name)
# print(b._PrivateAcc__accessType)

print(b.__dir__())