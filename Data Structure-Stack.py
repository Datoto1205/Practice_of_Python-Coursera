stack = []

def checkTheNumberOfElement(stack):
    return len(stack)

def pushNewElement(newElement):
    stack.append(newElement)

def popTheElement():
    return stack.pop(len(stack)-1)#stack[len(stack)-1]

print("The number of elements in the stack is:", checkTheNumberOfElement(stack))
pushNewElement(1)
print("The number of elements in the stack is:", checkTheNumberOfElement(stack))
pushNewElement(3)
print("The number of elements in the stack is:", checkTheNumberOfElement(stack))
pushNewElement(5)
print("The number of elements in the stack is:", checkTheNumberOfElement(stack))

print("The toppest element is:", popTheElement())
print("The number of elements in the stack is:", checkTheNumberOfElement(stack))
print("The toppest element is:", popTheElement())
print("The number of elements in the stack is:", checkTheNumberOfElement(stack))
print("The toppest element is:", popTheElement())
