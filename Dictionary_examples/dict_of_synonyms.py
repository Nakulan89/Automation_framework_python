synonym_dict = {'habitat': ['environment', 'surroundings', 'territory', 'home'],
         'clean': ['unsoiled', 'tidy', 'speckless','unsullied', 'unstained', 'spotless'],
         'majority': ['bulk', 'mass'],
         'strong': ['tough', 'hard', 'powerful', 'sturdy', 'burly', 'ironlike'],
         'weak': ['frail', 'puny', 'fragile', 'powerless']}

print('My synonyms dictionary :')
print('word list')
print('------------------')
for word in synonym_dict:
    print(word)
flag = False
input_word = input('Enter a word for its synonyms :')
for word, synonym in synonym_dict.items():
    if word == input_word:
        print(word, ':', synonym)
        flag = True
if not flag:
    print('word is not found')
