x = input("guess a number between 1-20")
import random
y = random.randint(1, 20)
i = 0

while i < 5:
    if x == y :
        print("right")
    elif x < y:
        print("the numder should be smaller")
    else:
        print("the number shuld be bigger")
i = i+1
    
    

