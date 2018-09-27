"""
This program demonstrates IMPORT statements and LOOPS
"""

# import satements fo FIRST! (TOP OF YOUR CODE)
import time
import random

# for variableName in rand(start,stop, step)
# OR
# for variableName in and(stop): *This will start at 0 and stop at 1

evens = 0
odds = 0
l_even = " Evens: "
l_odds = " Odds: "

for Thoe in range (10):
    rand = random.randint(-100, 100)
    if rand%2 == 0:
        evens += 1
        l_even = l_even+str(rand)+", "
    else:
        odds += 1
        l_odds = l_even+str(rand)+", "
print(str(evens)+l_even)
print(str(odds)+l_odds)