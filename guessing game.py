import random
randomint = random.randint(1, 100)

x = int(input ("Input a number between 1 - 100 :"))
print (x)

if x < 1 or x > 100 :
    print ("invalid input")
else :
    if x == randomint :
        print (x,"correct")
    else :
        print ("incorect, computer guessed :", randomint) 
