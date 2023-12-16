'''
write a python program to translate a message into secret code language. Use the rules below to translate normal english into secret code lang..
coding 
1. If the word contains atleast 3 characters, remove the first letter and append it at the end. 
2. Now append three random characters at the starting and the end
else:
simply reverese the string

Decoding...
if the word contains less then 3 characters reverse it
else:
remove 3 random characters from start and end. Now remove the last letter and append it to the beginning
'''
import random
import string 
# code :

def randomLetterGenerator():
        randomLetters = ''.join(random.choices(string.ascii_letters, k = 3))
        return randomLetters

# encode method here 
def encode():    
    sentence = input("Enter which you want to encode: ")
    arrOfSen = sentence.split(" ")
    for i in range(len(arrOfSen)):
        if(len(arrOfSen[i]) < 3):
            arrOfSen[i] = ''.join(reversed(arrOfSen[i]))
        else:
            firstL = arrOfSen[i][0]
            remeiningString = arrOfSen[i][1:]
            modifiedStr  = randomLetterGenerator() + remeiningString + firstL + randomLetterGenerator() 
            arrOfSen[i] = modifiedStr

        sentence = ' '.join(arrOfSen)
    print(f"Encode of the sentence you entered is: {sentence}")

# decode method here 
def decode():
    sentence = input("Enter which you want to decode: ")
    arrOfSen = sentence.split(" ")
    for i in range(len(arrOfSen)):
        if(len(arrOfSen[i]) < 3):
            arrOfSen[i] = ''.join(reversed(arrOfSen[i]))
        else:
            removeRandom = arrOfSen[i][3:-3]
            getLastLetter = removeRandom[-1:]
            removeLastLetter = removeRandom[0: -1]
            modifiedStr = getLastLetter + removeLastLetter
            arrOfSen[i] = modifiedStr
        sentence = ' '.join(arrOfSen)
    print(f"Decode of the sentence is: {sentence}")

            


ques = input("Which method do you want to use? For encode presse 1 and for decode press 2 : ")
if ques == "1":
     encode()
elif ques == "2":
     decode()

