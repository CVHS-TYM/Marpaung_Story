# Packages
import random

# Declare variables
rand = random.randint(1, 100)
print("Guess the integer between 1 and 100!")
tries = 0
z = ""
com = ""
while True:
    guess = float(input("The number is "))
    #Check if blank
    if guess == None:
        com = "blank. Put an actual number"
    
    # Check if its float or integer
    if guess%1 != 0 or guess%2 != 1:
        com = "not an integer"
    
    # Check if its within range and allow two exceptions
    elif guess < 1 or guess > 100 and guess != 33001 and guess != 33002:
        com = "not within 1 through 100"
    
    # Print the random number
    elif guess == 33001:
        print("\n\nHey how'd you get here >:((((\n"+str(rand)+"\n\n")
        z = " Cheater."
    
    elif guess < rand:
        com = "less"
    elif guess > rand:
        com = "greater"
    elif guess == rand:
        print("You got the correct answer in "+str(tries)+" tries."+z)
        break
    print("Your guess is "+com+"."+z)
    tries += 1
    continue