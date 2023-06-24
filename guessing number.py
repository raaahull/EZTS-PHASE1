import random 
n=random.randrange(1,50)
guess = int(input("enter any num:"))
while n!= guess:
    if guess < n:
        print("Too low")
        guess = int(input("enter any num again:"))
    elif guess > n:
        print("Too high")
        guess = int(input("enter any num again:"))
    else:
        break
print("you guessed it right!!")
