import re
pattern = r'\b M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3}) \b'

pat = re.compile(pattern,flags=0)
s = 'asd asdasds MCI adfd23e MMM 11'

for p in pat.finditer(s):
    print(p.group(), end = '')
