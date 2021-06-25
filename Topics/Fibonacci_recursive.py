def recur_fib(n):
    if n <= 1:
        return n
    else:
        return recur_fib(n-1) + recur_fib(n-2)


nterm = int(input("Enter the input integer value :"))
if nterm <= 0:
    print("Please enter the positive integer")
else:
    print("Fibonacci sequence:", end=" ")
    for i in range(nterm):
        print(recur_fib(i), end=" ")
