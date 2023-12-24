
'''
what is the differences between is or == 
is check the referece also... like that === in node.js
== just check the value, don't check reference
'''
a = 3 
b = 3 

print(a == b)
print(a is b)

a = [1,2,3]
b = [1,2,3]
print(a == b) # just check the value. return: True
print(a is b) #check the reference also. return: False