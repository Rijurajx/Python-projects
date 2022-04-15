import random
randNumber=random.randint(1,100)
userGuess=None
guesses=0
while (userGuess!=randNumber):
    userGuess=int(input("Enter your guess: "))
    guesses+=1
    if(userGuess==randNumber):
        print("you guessed it right!")
    else:
        if(userGuess>randNumber):
            print("you guessed it wrong..enter a smaller number")
        else:
            print("you guessed it wrong...enter a larger number")

print(f"you guessed the correct number in {guesses} guesses.")

with open("highscore.txt") as f:
    highscore=int(f.read())

if(guesses<highscore):
    with open("highscore.txt","w") as f:
        f.write(str(guesses))
