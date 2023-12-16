'''
Create a program capable of displaying questions to the user like KBC.
Use list data typeto store the questions and their correct answers.
Display the final amount of the person is taking home after playing the game.
'''
questions = [
    ["Who is the creator of Python?", "Guido van Rossum", "Larry Page", "Mark Zuckerberg", "Elon Musk", 0],
    ["What is the purpose of the 'if' statement in Python?", "Looping", "Conditionally executing code", "Defining a function", "Importing a module", 1],
    ["Which of the following is a mutable data type in Python?", "Tuple", "List", "String", "Dictionary", 1],
    ["What does the term 'PEP' stand for in Python?", "Python Enhancement Proposal", "Programming Efficiency Process", "Primary Execution Protocol", "Python Extension Pack", 0],
    ["How do you comment a single line in Python?", "# This is a comment", "// This is a comment", "-- This is a comment", "/* This is a comment */", 0],
    ["What is the purpose of the 'elif' keyword in Python?", "Defining a class", "Handling exceptions", "Concatenating strings", "Alternative condition in an 'if-else' statement", 3],
    ["In Python, how do you open a file in binary mode?", "file_open('filename', 'rb')", "open_file('filename', 'wb')", "open('filename', 'r')", "open('filename', 'rb')", 3],
    ["What is the role of the 'self' parameter in a class method?", "Refers to the instance of the class", "Specifies the class type", "Allows multiple inheritance", "Defines a static method", 0],
    ["Which module in Python is used for working with regular expressions?", "re", "regex", "regexp", "reg", 0],
    ["What is the purpose of the 'virtualenv' tool in Python?", "Virtual machine management", "Package management", "Environment isolation for Python projects", "Web development framework", 2]
]

levels = [
    [1, "₹1,000"],
    [2, "₹2,000"],
    [3, "₹5,000"],
    [4, "₹10,000"],
    [5, "₹20,000"],
    [6, "₹40,000"],
    [7, "₹80,000"],
    [8, "₹1,60,000"],
    [9, "₹3,20,000"],
    [10, "₹6,40,000"],
]
score = 0
money = 0
for i in range(0, len(questions)):
    question = questions[i]
    level = levels[i]
    print(f"Questions for Rs. {level}")
    print(f"Q-{i + 1}: {question[0]}")
    print(f"a. {question[1]}    b. {question[2]}")
    print(f"c. {question[3]}   d. {question[4]}\n")
    ans = input("What is the correct answer(write only 1/2/3/4): ") 
    if(ans == "q"):
        break
    elif((int(ans)-1) == question[5]):
        print(f"Your answer is correct. You will paid: {level}\n")
        score = score + 1
        if(i == 4):
            money = 10000
        elif (i == 8):
            money = 320000
    else:
        print(f"Wrong answer")
        break

print(f"Your total score is {score} out of {len(questions)}. And you will get Rs. {money}")
   

