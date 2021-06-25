num = int(input("Enter the integer value to find the factorial :"))
Factorial = 1

if num < 1:
    print("Sorry, negative values are not allowed")
elif num == 1:
    print("The factorial of 0 is 1")
else:
    print("The Factorial of {} is :".format(num), end=" ")
    for i in range(1, num + 1):
        Factorial = Factorial * i
    print(Factorial, end=" ")
