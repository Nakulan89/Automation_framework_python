def convert_to_binary(n):
    if n > 1:
        convert_to_binary(n // 2)
    print(n % 2, end=' ')


dec = 34
print("The Binary format for {} is : ".format(dec), end="")
convert_to_binary(dec)

