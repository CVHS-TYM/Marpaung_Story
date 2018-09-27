#1


#2
import random
#for a in range(500):
#    print(random.randint(0,100))
    
#3
#c = ""
#for i in range(100):
#    a = random.randint(0,100)
#    if a%2 == 0:
#        c = "even"
#    elif a%2 == 1:
#        c = "odd"
#    print(str(a)+" is "+c)

#4
#accidently pushed lol
evens = 0
l_evens = "Evens: "
for i in range(100):
    a = random.randint(0,100)
    if a%2 == 0:
        evens += 1
        l_evens = (l_evens+str(a)+" ")
print("There are "+str(evens)+" evens.")
print(l_evens)

#5
