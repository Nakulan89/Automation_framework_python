a = input("Enter the string to check whether it's palindrome : ")
b = a[::-1]
if a == b:
    print("{} and {} are palindrome".format(a, b))
else:
    print("{} and {} are not palindrome".format(a, b))
