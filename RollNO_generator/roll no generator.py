regNo = input("Enter the registration number : ")
a = [int (i) for i in regNo]
ab = [a[i:i+2] for i in range(0,len(a),2)]
abc = [max(ab[i]) for i in range(len(ab))]
string_ints = [str(int) for int in abc]
str_of_ints = "".join(string_ints)
print(f"Roll number generated is : {str_of_ints}")