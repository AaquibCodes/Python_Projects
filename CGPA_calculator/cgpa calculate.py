a = int(input("enter marks secured = "))
b = int(input("total marks ="))


def functions1(a, b):
    percentage = (a / b) * 100
    return percentage


def functions2():
    cgpa = functions1(a, b) / 8.8
    return cgpa


v = functions1(a, b)
print("the percentage is =", v)
x = functions2()
if functions2() > 10:
    print("the cgpa is = 10")
else:
    print("the cgpa is =  ", x)
if functions1(a, b) in range(0, 39):
    print("FAILED!!!!")
elif functions1(a, b) in range(40, 49):
    print("pass class")
elif functions1(a, b) in range(50, 55):
    print("second class")
elif functions1(a, b) in range(56, 59):
    print("higher second class")
elif functions1(a, b) in range(60, 69):
    print("first class")
else:
    print("first class with distinction")
