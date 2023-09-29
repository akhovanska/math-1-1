word1 = input()
word2 = input()

set1 = set(word1)
set2 = set(word2)
if set2.issubset(set1):
    print('Ok')
else:
    print('No')
