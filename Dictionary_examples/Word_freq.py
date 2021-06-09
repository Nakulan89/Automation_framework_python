input_sen = input('Please enter the sentence :').lower()
word = input_sen.split()
freq = {}

for w in word:
    freq[w] = freq.get(w, 0) + 1

print(freq)

