def bubble_sort(num):
    n = len(num)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]
    return num


x = [645, 55, 78, 100, 89, 43, 21]
print(bubble_sort(x))
