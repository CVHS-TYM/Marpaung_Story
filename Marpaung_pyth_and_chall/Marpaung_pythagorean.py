print("IDE: What's your name?\n")
name = input("My name is ")
print("\nIDE: Hello "+name+".")

print("I'm trying to make a pythagorean triangle, help me out.")
print("Also, I'm using a calculator so I'd appreciate 1,2,3... and not one,two,three...")
print("\nOkay! So just go ahead and give me the \"a\" and the \"b\"")

val_a = float(input("a = "))
val_b = float(input("b = "))

val_c = ((val_a**2+val_b**2)**.5)

print("\nIDE: Okay, let's do some math.")
print("a² + b² = c²")
print(str(val_a)+"² + "+str(val_b)+"² = c²")
print(str(val_a**2)+" + "+str(val_b**2)+" = c²")
print(str(val_a**2+val_b**2)+" = c²")
print("√"+str(val_a**2+val_b**2)+" = c")
print("The hypotenuse, c, equals "+str((val_a**2+val_b**2)**.5))