import re

PATTERN_VOWELS = r"[аоеуиієюяїАОЕУИІЄЮЯЇ]+"
def func(words):
    s = ""
    for word in words:
        if len(word) > 2:
            s += re.sub(PATTERN_VOWELS, "", word)
            s += " "
        else:
            s += word
            s += " "
    return s
f = open('File.txt', 'r', encoding = 'utf-8')
text = f.read()
print(re.sub(PATTERN_VOWELS, "", text))
#print(re.split(r'\s+', text))
words = re.split(r'\s+', text)
print(func(words))


f.close()
