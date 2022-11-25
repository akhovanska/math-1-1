s = input()

counter = 0
for ch in s[1:]:
    if ch == "+" or ch == "-" or ch == "*":
        counter += 1

print(counter)
