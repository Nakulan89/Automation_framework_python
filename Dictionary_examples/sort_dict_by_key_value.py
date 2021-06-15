import operator

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print('Original dictionary : ', d)
sorted_key = sorted(d.items(), key=operator.itemgetter(0))
sorted_value = sorted(d.items(), key=operator.itemgetter(1))
st = iter(sorted_key)
dt = iter(sorted_value)
print("Dictionary in ascending order by key : ", dict(zip(st, st)))
print("Dictionary in descending order by value : ", dict(zip(dt, dt)))



