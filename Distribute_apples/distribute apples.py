n = int(input("Enter the number of apples : "))
b = input("Enter the range with a (-) of peoples you want to distribute between ? -- ").split("-")
mn = int(b[0])
mx = int(b[1])
for i in range(mn,mx+1):
    if n%i == 0:print(f"{n} apples can be divided equally among {i} people ")
    if n%i != 0:print(f"{n} apples cannot be divided equally among {i} people ")
    i += 1
