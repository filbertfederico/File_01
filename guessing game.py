import random
randomint = random.randint(1, 100)

x = int(input ("Input a number between 1 - 100 :"))

while x != "randomint":
    if x > 1 or x < 100 :
        if x == randomint :
            print ("correct")
            break
        elif x < randomint :
            print ("too low")
            x = int(input ("Input a number between 1 - 100 :"))
        elif x > randomint :
            print ("too high")
            x = int(input ("Input a number between 1 - 100 :"))
        else :
            print ("incorrect input")    
