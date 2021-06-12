s = 123456789

rev_number = 0
while s > 0:
    remainder = s % 10
    rev_number = (rev_number * 10) + remainder
    s = s // 10

print("The reverse number is :{}".format(rev_number))




