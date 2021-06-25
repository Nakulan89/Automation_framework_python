num = 1634
order = len(str(num))
s = 0
temp = num
while temp > 0:
    digit = temp % 10
    print(digit)
    s += digit ** order
    print(s)
    temp //= 10

if num == s:
    print(num, "is an Armstrong number")
else:
    print(num, "is not a Armstrong number")
