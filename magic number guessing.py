from random import randint          #Importing random for guessing a number
from time import sleep              #Importing sleep for take a time between runnning a programm

while True:                         # Starting A While loop

    magicNumber=randint(0,10)       #this is magicNumber Variable Who hold random number means magicNumber
    
    print("""
    Please Enter Number Between Than And Equal To 0 And 10
    If Your Number Is Equal To magicNumber Than You Won Else You Play Again
    """)

    user_input=int(input(" : "))    #Here Is User Enter A Number 
    if user_input>10:               #This If Function Is Doing if Your Nunber Is Greater Than 10 Than Your Programm Is Not Running
        print("Your Number Is Greater Than 10 Please Try Again ")

    else:
        print()
        print("Your Number Is ......")
        sleep(2)
        print("Your Number Is " + str(user_input))
        print()
        sleep(1)
        print("Magic Number Is.......")
        sleep(3)
        print("Magic Number Is " + str(magicNumber))
        print()


        if user_input==magicNumber:     #This If Function Is Doing If User_number is Equal Thann magicNumber Than You Won
            sleep(2)
            print("You Won This game")

        else:
            sleep(2)
            print("You Lose This game")

        print()
        sleep(2)
        print("Loading To Play Again Game")
        sleep(1)
        print()
        print("You Want To Play This Game Then Enter [y] Else Enter[n]? ")
        print()
        sleep(1)
        user=input(" : ")
        if user=="y":      # If User Enter "y" Then Programm Run Again
            sleep(1)
            print("Starting A Game")

        elif user=="n": # If User Enter "n" Then Programm Close
            break

    
            



