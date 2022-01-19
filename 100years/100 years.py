def age():
    abc = (input("Enter your age or birth year: "))
    if len(abc) <= 3:
        print("You will turn 100 in the year",2021 + (100 - int(abc)))
    elif len(abc) == 4:
        print("You will turn 100 in the year",int(abc) + 100)
    else :
        print("invalid input")

if __name__ == '__main__':
    age()