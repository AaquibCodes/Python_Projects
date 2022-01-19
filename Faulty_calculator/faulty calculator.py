#45 * 3 = 555
#56+9 = 77
#56/6 = 4

a=int(input("enter a number ="))
b=(input("select a operator [ % , * , + , - ]"))
c=int(input("enter a number ="))
if a == 45 and c == 3 :
    if b == "*" :
        print("555")
elif a == 56 and c == 9 :
    if b == "+" :
        print("77")
elif a == 56 and c == 6 :
    if b == "/" :
        print("4")
elif b == "+" :
    print(" = ",a+c)
elif b == "-" :
    print(" = ",a-c)
elif b == "*" :
    print(" = ",a*c)
elif b == "/" :
    print(" = ",a/c)