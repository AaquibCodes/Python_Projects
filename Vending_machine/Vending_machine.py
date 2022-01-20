import time


def log():
    print(time.asctime(time.localtime(time.time())))


class Vending_machine:

    def __init__(self, items, cost):
        self.items = items
        self.cost = cost

    def want(self):
        try:
            req_items = int(input("\nHow many Coco-Cola's do you want : "))
            if req_items > self.items:
                with open("Vending_machine_log.txt", "r+") as f:
                    f.write(time.asctime(time.localtime(time.time())) + " : User asked for more cans than the stock.")
                print(f"Sorry we have only {self.items} Coca-Cola's in our machine.")

            elif req_items <= self.items:
                money = int(input(f"Pay Rs {req_items * self.cost} : "))
                if money >= req_items * self.cost:
                    change = money - req_items * self.cost
                    print(f"Here's your change : Rs {change}")
                    self.items = self.items - req_items
                    print(f"\nCoca-Cola's left in the machine : {self.items}")
                    with open("Vending_machine_log.txt", "a") as f:
                        f.write(str(time.asctime(time.localtime(time.time()))) + " : Sold " + str(
                            req_items) + " cans -- Money received Rs " + str(money) + " : Change returned Rs " + str(
                            change) + "\n")
                    if self.items == 0:
                        print("\n* * * ThankYou for using our Vending Machine -- Our machine has run out of cans  "
                              "* * *")
                        exit()

                else:
                    print(f"Sorry you don't have enough money")
            question()

        except ValueError:
            print("INVALID INPUT !!!")


def question():
    while True:
        a = input("\nYou want more Cola's (Y/N) : ").upper()
        if a == "Y":
            break
        elif a == "N":
            print("\n* * * ThankYou for using our Vending Machine * * *\n")
            exit()
        else:
            print("INVALID INPUT !!! .... Try Again")
            continue


if __name__ == '__main__':
    print("\n\t\t\t $ Welcome to our Coca-Cola Vending Machine $ ")
    Coca_Cola = Vending_machine(100, 20)
    print(f"\nOur Vending Machine stores {Coca_Cola.items} Coca-Cola's")
    while True:
        Coca_Cola.want()
