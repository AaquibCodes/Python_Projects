from datetime import datetime
from json.tool import main
from threading import main_thread
from typing import List


def getdate():
    import datetime
    return datetime.datetime.now()

print("\n\t\tWelcome to Health Management System\t\t\n".upper())
members = ["Vidhut", "John", "Kat"]
time = getdate()
print("Do you want to Log or Retrieve Data ?\n")
while True:
    step1 = input("Press 1 [log] or Press 2 [Retrieve] or Press 3 [Exit].\n")
    if step1 == "1":
        print("Whose data do you want to log ? ", members)
        a = input()
        a1 = a.capitalize()
        if a1 == "Vidhut":
            a2 = input("Do you want to log Diet or Workout ?\n")
            A2 = a2.capitalize()
            if A2 == "Diet":
                f = open('Diet_Vidhut.txt', "a")
                Food = input("Type Here\n")
                f.write(str(time) + " : " + Food + "\n")
                print("successfully written")
                continue
            elif A2 == "Workout":
                f = open('Workout_Vidhut.txt', "a")
                Workout = input("Type Here\n")
                f.write(str(time) + " : " + Workout + "\n")
                print("successfully written")
                continue
        elif a1 == "John":
            a2 = input("Do you want to log Diet or Workout ?\n")
            A2 = a2.capitalize()
            if A2 == "Diet":
                f = open('Diet_john.txt', "a")
                Food = input("Type Here\n")
                f.write(str(time) + " : " + Food + "\n")
                print("successfully written")
                continue
            elif A2 == "Workout":
                f = open('Workout_john.txt', "a")
                Workout = input("Type Here\n")
                f.write(str(time) + " : " + Workout + "\n")
                print("successfully written")
                continue
        elif a1 == "Kat":
            a2 = input("Do you want to log Diet or Workout ?\n")
            A2 = a2.capitalize()
            if A2 == "Diet":
                f = open('Diet_Kat.txt', "a")
                Food = input("Type Here\n")
                f.write(str(time) + " : " + Food + "\n")
                print("successfully written")
                continue
            elif A2 == "Workout":
                f = open('Workout_kat.txt', "a")
                Workout = input("Type Here\n")
                f.write(str(time) + " : " + Workout + "\n")
                print("successfully written")
                continue
    elif step1 == "2":
        print("Whose data do you want to Retrieve ? ", members)
        a = input()
        a1 = a.capitalize()
        if a1 == "Vidhut":
            a2 = input("Do you want to retrieve Diet or Workout ?\n")
            A2 = a2.capitalize()
            if A2 == "Diet":
                f = open('Diet_Vidhut.txt', "r")
                print(f.read())
                continue
            elif A2 == "Workout":
                f = open('Workout_Vidhut.txt', "r")
                print(f.read())
                continue
        elif a1 == "John":
            a2 = input("Do you want to retrieve Diet or Workout ?\n")
            A2 = a2.capitalize()
            if A2 == "Diet":
                f = open('Diet_john.txt', "r")
                print(f.read())
                continue
            elif A2 == "Workout":
                f = open('Workout_john.txt', "r")
                print(f.read())
                continue
        elif a1 == "Kat":
            a2 = input("Do you want to retrieve Diet or Workout ?\n")
            A2 = a2.capitalize()
            if A2 == "Diet":
                f = open('Diet_Kat.txt', "r")
                print(f.read())
                continue
            elif A2 == "Workout":
                f = open('Workout_kat.txt', "r")
                print(f.read())
                continue
    elif step1 == "3":
        print("Thankyou for using our Health Management System")
        break

