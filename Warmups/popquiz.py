#1


#2
import random
#for a in range(500):
#    print(random.randint(0,100))
    
#3
c = ""
a = random.randint(0,100)
if a%2 == 0:
    c = "even"
elif a%2 == 1:
    c = "odd"
print(str(a)+" is "+c)