import random
rand = random.randint(1, 100)

print("Guess the integer between 1 and 100!")
guess = int(input("The number is "))
diff = abs(rand-guess)
if guess < rand:
    com = " less than "
elif guess > rand:
    com = " greater than "
elif guess == rand:
    com = "exactly "
    diff = ""
print("Your guess "+str(guess)+" was "+str(diff)+com+str(rand)+".")