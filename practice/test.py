# This module is used to keep you in the cmd window
# Not needed if using an IDE
from msvcrt import getch

print("\n#### This program finds the requested keyword and returns the line above it #### \n"
      "Note - The Keyword is case sensitive.\n")

File = input(r"Enter the name or path of the file : ")
String = input("Keyword : ")

index = 0

f =  open(File,'r')
lines = f.readlines()
# print(lines)
for xyz in lines:
    index += 1
    if String in xyz    :
        print("\nThe line above your requested keyword is :\n Line number ",index-1," Output : ",lines[index-2])
    # else:
    #     print("\nKeyword not found ! ! !")
    #     break
f.close()
#This funtion is used to keep you in the cmd window
# Not needed if using an IDE
getch()
