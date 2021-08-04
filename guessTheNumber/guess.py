import random

a = random.randrange(20)
print(a)
flag = 0
while(True):
    guess = int(input("Enter a number :"))
    if(guess > a):
        print("Lower")
    elif(guess < a):
        print("Upper")
    elif(guess == a):
        print("You Won !!! with the this number ---->   " + str(a))
        break
