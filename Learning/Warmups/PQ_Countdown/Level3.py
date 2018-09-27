import time

a = int(input("Choose a number to countdown: "))
for i in range(a+1):
    time.sleep(1)
    print(a-i)