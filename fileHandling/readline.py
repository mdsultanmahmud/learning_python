# f = open("myfile2.txt", 'r')

# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)

file = open("myfile2.txt", 'w')
lines = ["line1\n", "line2\n", "line3\n"]
file.writelines(lines)
file.close()