def min_max(x):
    minimum = maximum = x[0]
    for i in x[1:]:
        if i < minimum:
            minimum = i
        else:
            if i > maximum:
                maximum = i
    return minimum, maximum


input_value = [3, 5, 1, 6, 9, 12, 56]
print(min_max(input_value))