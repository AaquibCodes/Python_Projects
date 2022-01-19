a = int(input())
b = int(input("Enter 1 or 0 = "))
i = 1
if b == 1:
    while i <= a:
        print("*\t" * i)
        i = i + 1

elif b == 0:
    while i <= a:
        print("*\t " * a)
        a = a - 1

else:
    print("enter the correct boolean")
