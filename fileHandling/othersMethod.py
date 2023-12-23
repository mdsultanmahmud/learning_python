# with open("myfile2.txt", 'r') as f:
#     print(type(f))
#     f.seek(10)
#     print(f.tell())
#     data = f.read()
#     print(data)


with open("myfile3.txt", 'w') as f:
    f.write("Hello programmer")
    f.truncate(10)

with open("myfile3.txt", 'r' ) as f:
    print(f.read())