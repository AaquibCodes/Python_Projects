import random

def good_dice():
        a = [1,2,3,4,4,5,5,5,6,6,6,6,]
        return random.choice(a)

def bad_dice():
        a = [1,1,1,1,2,2,2,3,3, 4, 5, 6]
        return random.choice(a)

if __name__ == '__main__':
    a = int(input("Do you want a favourable dice or a unfavourable dice ?\nPress 1 for favourable and 2 for unfavourable -- "))
    if a == 1:
        while True:
            b = int(input("press 0 to roll the dice : "))
            if b == 0 : print(good_dice())
    if a == 2:
        while True:
            b = int(input("press 0 to roll the dice : "))
            if b == 0: print(bad_dice())


