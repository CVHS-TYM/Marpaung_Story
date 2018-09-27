import random

def EvenOdd():
    evens = 0
    l_evens = "Evens: "
    for i in range(100):
        a = random.randint(0,100)
        if a%2 == 0:
            evens += 1
            l_evens = (l_evens+str(a)+" ")
    print("There are "+str(evens)+" evens.")
    print(l_evens)
    
def greeting():
    print("What's your name?")
    name = input("My name is ")
    print("Hi, "+name)
    
def age():
    age = int(input("What's your age? "))
    return age