# DECLARATION
# Hello World
firstString = "hello"
secondString = ", python!\t"
print(firstString + secondString)

# Combine Strings
print("\n")
assembledString = firstString + secondString + "\t"
print(2*(assembledString))

# Length of String
numberOfString = len(firstString)
print("\nThe length of the firstString is: ", numberOfString, "\n")

numberOfRepeatedString = assembledString.count("o")
print("The letter \"o\" in the firstString repeated for ", numberOfRepeatedString, " times.")

# Integer
firstInteger = 5
secondInteger = 2
print(firstInteger)
MultipliedResult = firstInteger*secondInteger

print(str(firstInteger) + " muitiply " + str(secondInteger) + " equal to " + str(MultipliedResult))
# I need to transfer integer into string through the function str() if I want to print integer with string together.

# Bool
firstBool = bool(0)
secondBool = bool(2)
print("\n0 means " + str(firstBool) + " in python")
print("The number over than 0 means " + str(secondBool) + " in python")

# Array
firstArray = [1, 2, 3, 4, 5]
print("The second element in the firstArray is: " + str(firstArray[1]))
print("The number of elements in the firstArray is: " + str(len(firstArray)))

firstArray.append(6)
print("\nThe new element is: " + str(firstArray[5]))
firstArray.remove(6)
print("The length of firstArray has been returned to: " + str(len(firstArray)))

print("\nThe max element in firstArray is: " + str(max(firstArray)))
print("The sum of every elements in firstArray is: " + str(sum(firstArray)))

ls = list()
ls

# Slice of An Array
secondArray = firstArray[1:3]
print(secondArray)

# Dictionary
firstDic = {}
firstDic["firstGirlfriend"] = "Cindy"
firstDic["secondGirlfriend"] = "Tina"
firstDic["thirdGirlfriend"] = "Betty"

# Search Value with Key
print("The length of my firstDictionary is: " + str(len(firstDic)))
print("The second element of firstDic is: " + str(firstDic["secondGirlfriend"]))

# Search Key with Value
for key in firstDic:
    if firstDic[key] == "Betty":
        print("\n" + str(key))

print(firstDic.get("firstGirlfriend", "Error"))
print("\n")

# Use Error Type to Prevent Crash
try:
    print(firstDic["secondGirlfriend"])
    print(firstDic["forthGirlfriend"])
except KeyError:
    print("No value!")

# Use .setdefault function to do the same thing
print(firstDic.setdefault("secondGirlfriend", "No value!"))   # If the value of particular key exist, return the value, or return default value "No value!".
print(firstDic.setdefault("forthGirlfriend", "No value!"))

#CONTROL FLOW
# Loop
for i in range(1, 10) :
    for j in range(2, 9) :
        if j == 8:
            print(str(j) + " * " + str(i) + " = " + str(i*j))
        else:
            print(str(j) + " * " + str(i) + " = " + str(i*j), end = '\t')

# Input
answer = 4
userWinTheGame = bool(0)

print("\nPlease guess a number between 0 to 5. You could guess for three times.")
for i in range(1, 4):
    userInpu = int(input())
    if userInpu == answer:
        print("\nBingo!")
        userWinTheGame = bool(1)
        break
    else:
        if i != 3:
            print("\nPlease guess again")

if userWinTheGame == 0:
    print("\nGame over!")

# If & Function with Input and Output
def firstFunction(numberOfMyGirlfriend):
    if numberOfMyGirlfriend == 0:
        return "I am single"
    else:
        return "I am not single"

print(firstFunction(5) + "\n")

# Function with Input of Array
def seeTheArray(inputArray):
    for i in range(0, len(inputArray)):
        print(inputArray[i])

seeTheArray(firstArray)
print("\n")

# Find
target = ["bee", "zoo", "beneficial", "face", "close", "efficient"]
criteria1 = "be"
criteria2 = "o"
criteria3 = "fi"
for i in range(0, len(target)):
    if target[i].find(criteria1) == -1:
        if target[i].find(criteria2) == -1:
            if target[i].find(criteria3) == -1:
                print("Did not find anything!")
            else:
                print("Find ", criteria3, " successfully!")
        else:
            print("Find ", criteria2, " successfully!")
    else:
        print("Find ", criteria1, " successfully!")

# Generate Random Number
import random

randomMatrix = []
for i in range(0, 50):
    randomMatrix.append(random.randint(0, 50000))

print(randomMatrix)

# While
a = 0

while True:
    while a < 3:
        print("The code \"while True\" means \"always\" I guess, I should stop it!")
        a += 1

# Note with Multipal Lines
'''
    I could press "control" and "/" to create note with multipal lines.
'''

# None and is
strangeNumber = None    # None is a kind of "flag type".
strangeBul = True

for i in range(0, 2):
    if strangeNumber is None:
        print(type(strangeNumber))
        strangeNumber = 1
    else:
        print(type(strangeNumber))

    if strangeBul is True:  # "is" was used for boolean and None, it is similar to "==".
        print("Yes")
        strangeBul = False
    else:
        print("No")
        strangeBul = True

# Read A File
'''
fileHandle= open("THE NAME OF YOUR FILE.txt", 'r')      # open() could open a file and store it in the memory,
                                                        "print(fileHandle)" only shows the address. Make sure
                                                        that the file of this python codes and the file you
                                                        want to read (here is .txt file) should be put in the
                                                        same place.
data = fileHandle.read()                                # read() could transfer the file handle into readable data.

for eachLine in data:                                   # Run through each line in the data.
    print(eachLine.rstrip())                            # rstrip() could be used to remove some useless "\n".

    if eachLine.startswith("From:") is True:            # .startwith() method could be used to check specific syntax, it would return a boolean.
        print("Find it!")
'''

# Split Sentence
sentence = "I love you!"
seperatedWords = sentence.split()       # .split() method could be used to split the words.
print(seperatedWords[1])
