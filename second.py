print("IDE: Are you old enough to vote? Tell me in a number, I ain't that smart.");
age = int(input("ME: My age is "));
if age < 18:
    print("\nIDE: Yeah... you're not old enough to vote.");
    print("IDE: Come back around in "+str(18-age)+" years.");
elif age >= 18:
    print("\nIDE: Who ya gonna vote for? Don't tell me I don't care.");