input_integer = int(input("Enter the integer to get the fib sequence : "))

n1, n2 = 0, 1
count = 0

if input_integer < 0:
    print("Pleas enter the positive integer :")
elif input_integer == 1:
    print("The fib sequence for {} is {}".format(input_integer, n1))
else:
    print("Fib sequence is :", end=" ")
    while count < input_integer:
        print(n1, end=" ")
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1

