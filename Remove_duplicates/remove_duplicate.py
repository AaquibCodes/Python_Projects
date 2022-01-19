def remove():
    n = int(input("Enter the range - "))
    list = []
    for i in range(n):
        a = int(input(" : "))
        list.append(a)
    final_list=[]
    for num in list :
        if num not in final_list:
            final_list.append(num)
    print(' '.join(map(str, final_list)))

if __name__ == '__main__':
    remove()
    print("The duplicates are removed!")