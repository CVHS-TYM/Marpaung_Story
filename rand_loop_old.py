import random
rand = random.randint(1, 100)

print(rand)
print("Guess the integer between 1 and 100!")
while True:
    guess = int(input("The number is "))
    diff = abs(rand-guess)
    if guess < rand:
        print("Less than")
    elif guess > rand:
        print("Greater than")
    elif guess == rand:
        print("Equal to")
        break
    print("a")
    continue
    