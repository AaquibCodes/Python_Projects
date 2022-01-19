n = int(input())
l1 = []
for i in range (n):
    a = int(input())
    l1.append(a)
    l1.remove(max(l1))
    print(max(l1))