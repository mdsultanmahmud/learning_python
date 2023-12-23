'''
for read file: r
for write file: w
for 
'''
# f = open("myfile.txt", 'r')
# f = open("myfile.txt")
# text = f.read()
# print(text)

# f.close()

# file2 = open("myfile2.txt", 'a')
# # file2.write("wow, i have created a file and enter some text by python!!! that's good!")
# file2.write("I can add which I want!!")
# file2.close()
# file2 = open("myfile2.txt")
# print(file2.read())

with open("myfile2.txt" ,'a') as f: 
    f.write("\nI'm adding another line of code!!")