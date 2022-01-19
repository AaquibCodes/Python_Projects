def fizzBuzz(n):
    # Write your code here
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 != 0:
            print("Fizz")
            continue
        elif i % 3 != 0 and i % 5 == 0:
            print("Buzz")
            continue
        elif i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
            continue
        print(i)

fizzBuzz(100)

