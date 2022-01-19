import random
import time

def times():
    return time.asctime(time.localtime(time.time()))

def randomchoice():
    a = int(input("From : "))
    b = int(input("To : "))
    list = [i for i in range(a,b)]
    return random.choice(list)#;print(choice)

if __name__ == '__main__':

    while True :
        print("\nEnter a range to start the game")
        choice = randomchoice()

        print("\nPlayer 1 -- You have 3 chances to guess the number.")
        for i in range(3):
            player1 = int(input(": "))
            if player1 == choice:
                print(f"You guess the right number in {i+1} chances")
                break
            elif player1 > choice:
                print(f"You guessed number is greater -- You have {2-i} chances left")
            elif player1 < choice:
                print(f"You guessed number is smaller -- You have {2-i} chances left")
            i += 1


        print("\nPlayer 2 -- You have 3 chances to guess the number.")
        for j in range(3):
            player1 = int(input(": "))
            if player1 == choice:
                print(f"You guess the right number in {j + 1} chances")
                break
            elif player1 > choice:
                print(f"You guessed number is greater -- You have {2 - j} chances left")
            elif player1 < choice:
                print(f"You guessed number is smaller -- You have {2 - j} chances left")
            j += 1

        if i < j :
            with open("Score.txt","a") as f:
                f.write(f"{times()} PLayer 1 WON -- guessed the number in {i+1} chances" + "\n")
            print("\nPlayer 1 WON")
        elif i > j:
            with open("Score.txt","a") as f:
                f.write(f"{times()} PLayer 2 WON -- guessed the number in {j+1} chances" + "\n")
            print("\nPlayer 2 WON")
        elif i == j:
            with open("Score.txt","a") as f:
                f.write(f"{times()} Its a Draw" + "\n")
            print("\nIt's a DRAW")

        bored = input("\nEnter [C] to continue or [E] to exit : ").upper()
        if bored == "C" :
            continue
        if bored == "E" :
            exit()


