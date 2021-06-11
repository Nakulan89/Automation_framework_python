n = int(input("Enter the number of elements in the list : "))
input_list = []
for i in range(0, n):
    input_list.append(int(input()))

print("Elements in the list before reversing :", input_list)

for i in range(n//2):
    temp = input_list[i]
    input_list[i] = input_list[n-i-1]
    input_list[n-i-1] = input_list[i]

print("Elements in the list after reversing :", input_list)
