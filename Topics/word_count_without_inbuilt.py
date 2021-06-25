def word_count(string, word):
    a = string.split()
    count = 0
    for i in range(0, len(a)):
        if word == a[i]:
            count = count + 1
    return count


st = str(input("Type any sentence to find the count of occurrence of a word : ").lower())
word = str(input("Please enter the word to find from the sentence :").lower())
print(word_count(st, word))
