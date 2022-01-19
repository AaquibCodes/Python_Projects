import random
import pyfiglet
from msvcrt import getch

title = pyfiglet.figlet_format("STONE PAPER SCISSOR",font="digital")
print(title)
print("\t\tWelcome to the Game\n")
print("Rules - \n"
      "#There will be 5 rounds\n"
      "#Stone kills Scissor || Scissor kills Paper || Paper kills Stone\n")

game = ["Stone", "Paper", "Scissor"]
Ascore = 0
Bscore = 0
i = 1
while i <= 5:
    choice = random.choice(game)
    print("Round - ",i)
    a = input("Enter a choice -  ")
    you = a.capitalize()
    print("Computers choice - ",choice)

    if choice == "Scissor" and you == "Stone":
        print("You Won")
        Ascore= Ascore + 1
        i = i + 1
        print("==============================================================================================")

    elif choice == "Stone" and you == "Paper":
        print("You Won")
        Ascore = Ascore + 1
        i = i + 1
        print("==============================================================================================")


    elif choice == "Paper" and you == "Scissor":
        print("You Won")
        Ascore = Ascore + 1
        i = i + 1
        print("==============================================================================================")

    elif choice == "Stone" and you == "Scissor":
        print("You Lose")
        Bscore = Bscore + 1
        i = i + 1
        print("==============================================================================================")

    elif choice == "Paper" and you == "Stone":
        print("You Lose")
        Bscore = Bscore + 1
        i = i + 1
        print("==============================================================================================")


    elif choice == "Scissor" and you == "Paper":
        print("You Lose")
        Bscore = Bscore + 1
        i = i + 1
        print("==============================================================================================")


    elif choice == you:
        print("Draw")
        i = i + 1
        print("==============================================================================================")


    else :
        print (" Enter a valid choice ")
        print("==============================================================================================")

Score = pyfiglet.figlet_format("SCORE BOARD",font=("digital"))
print(Score)
print("Computer", Bscore, "\tYou", Ascore)
if Ascore > Bscore :
    print("Winner Winner Chicken Dinner !!!!!")
elif Ascore < Bscore :
    print("You Lost !!!!!")
else :
    print("Draw")

getch()
