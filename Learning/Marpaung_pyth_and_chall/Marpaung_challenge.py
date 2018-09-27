print("Provide the three legs of a triangle. Numbers only.")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
legs = (a**2+b**2)

if (a+b <= c) :
    print("ERROR: This is not a real triangle.")
    print("\"a\" and \"b\" must not be equal or less than \"c\".")
else:
    if (legs == c**2):
        d = ("a right")
    elif (legs < c**2):
        d = ("an obtuse")
    elif (legs > c**2):
        d = ("an acute")
    print("This is "+d+" triangle.")