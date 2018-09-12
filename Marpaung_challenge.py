print("Provide the three legs of a triangle.")
a = input("a = ")
b = input("b = ")
c = input("c = ")

if (a+b) < c:
    print("This doesnt work")
if (a+b > c) or (a+b == c):
    print("This works")
    
#https://stackoverflow.com/questions/843277/how-do-i-check-if-a-variable-exists