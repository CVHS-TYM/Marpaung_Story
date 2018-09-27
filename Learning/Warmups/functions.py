"""
This is how functions working
"""

def greeting():     #This function does NOT return anything
    print("Hello World")

def askName():
    name = input("What is your name? ")
    return name
    
def askAge():       #Write a function that asks and returns how old they are
    age = int(input("What's your age? "))
    return age
    
def canVote(age):      #Write a function that takes their age IN and responds appropriately if they can or cannot vote
    if age() < 18:
        print("You can not vote.")
        canVote = False
    else:
        print("You can vote.")
        canVote = True
    return canVote

#Call functions
greeting()
x = askName() #Save output of askName() to variable
print("Hello "+x)

#Call the function and save to a variable
y = askAge()
z = canVote(y)
print(z)