import random
import os

replay = ""
while replay!="q":
    def readHighScore():
        with open ("highscore.txt","r") as f:
            temp = f.read()
            if temp == "":
                return 100
            else:
                return int(temp)

    def dashboard(high_score,user_score,lower_guess,upper_guess):
        hyphens = 78
        
        if high_score == 1:
            hgv = "1 Guess"
        else:
            hgv = f"{high_score} Guesses"
        if user_score == 1:
            ugv ="1 Guess"
        else:
            ugv = f"{user_score} Guesses"
        
        os.system("cls")
        print("\t\t\t***RANDOM GUESSER***")
        print("-"*hyphens)
        print(f"High Score : {hgv}\t\t\t\t\tGuess Range: [{lower_guess},{upper_guess}]")
        print(f"Your Score : {ugv}")
        print("-"*hyphens)

    def updateHighScore(user_score):
        with open ("highscore.txt","w") as f:
            f.write(str(user_score))
        
    def winScreen(high_score,user_score,user_guess):
        hyphens = 78
        
        if high_score == 1:
            hgv = "1 Guess"
        else:
            hgv = f"{high_score} Guesses"
        if user_score == 1:
            ugv ="1 Guess"
        else:
            ugv = f"{user_score} Guesses"

        os.system("cls")
        print("\t\t\t***RANDOM GUESSER***")
        print("-"*hyphens)
        print(f"Your Guess '{user_guess}' was Correct !!\n")
        print(f"Your Score : {ugv}")
        print(f"High Score : {hgv}")
        
        if user_score<high_score:
            print("\nNew High Score Updated !!")
            print(f"New High Score : {user_score}")
            updateHighScore(user_score)

        print("-"*hyphens)

    def resetHighScore():
        with open ("highscore.txt","w") as f:
            f.write ("")

    user_score = 0
    high_score = readHighScore()

    lower_guess =0
    upper_guess = 100
    temp_lower = 0
    temp_upper = 100

    user_guess = 0
    comp_num=random.randint(1,99)

    while user_guess!=comp_num:
        
        user_score = user_score + 1
        
        dashboard(high_score,user_score,lower_guess,upper_guess)
        if user_score == 1:
            print ("Guess a number between 1 and 99 : ",end = "")
        
        else:
            if user_guess > comp_num:
                if user_guess < temp_upper:
                    print ("Enter Lower number : ",end = "")
                    temp_upper = user_guess
                elif user_guess >= temp_upper:
                    print ("Guess the number using Guess Range : ",end = "")

            elif user_guess < comp_num:
                if user_guess > temp_lower:
                    print ("Enter Higher number : ",end = "")
                    temp_lower = user_guess
                elif user_guess <= temp_lower:
                    print ("Guess the number using Guess Range : ",end = "")

        user_guess = int(input())
        
        if user_guess > comp_num and user_guess < upper_guess:
            upper_guess = user_guess
        
        if user_guess < comp_num and user_guess > lower_guess:
            lower_guess = user_guess


    winScreen(high_score,user_score,comp_num)

    replay = input ("Play Again?\nPress 'Enter' to continue,\nPress 'q' to quit,\nPress 'r' to reset High Score\n"+("-"*78)+"\n").lower()
    if replay=="r":
        resetHighScore()

os.system("cls")

print("-"*78)
temp_input = input("Thanks for playing. Visit Again !!\n"+("-"*78)+"\n")