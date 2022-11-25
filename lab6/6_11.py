str = input()
k = 0
for n in range(0, len(str)):
	if str[n] == 'q' or str[n] == 'w' or str[n] == 'e' or str[n] == 'r' or str[n] == 't' or str[n] == 'y' or str[n] == 'u' or str[n] == 'i' or str[n] == 'o' or str[n] == 'p' or str[n] == 'a' or str[n] == 's' or str[n] == 'd' or str[n] == 'f' or str[n] == 'g' or str[n] == 'h' or str[n] == 'j' or str[n] == 'k' or str[n] == 'l' or str[n] == 'z' or str[n] == 'x' or str[n] == 'c' or str[n] == 'v' or str[n] == 'b' or str[n] == 'n' or str[n] == 'm':
		k = k + 1
		break
for n in range(0, len(str)):
	if str[n] == 'Q' or str[n] == 'W' or str[n] == 'E' or str[n] == 'R' or str[n] == 'T' or str[n] == 'Y' or str[n] == 'U' or str[n] == 'I' or str[n] == 'O' or str[n] == 'P' or str[n] == 'A' or str[n] == 'S' or str[n] == 'D' or str[n] == 'F' or str[n] == 'G' or str[n] == 'H' or str[n] == 'J' or str[n] == 'K' or str[n] == 'L' or str[n] == 'Z' or str[n] == 'X' or str[n] == 'C' or str[n] == 'V' or str[n] == 'B' or str[n] == 'N' or str[n] == 'M':
		k = k + 1
		break
for n in range(0, len(str)):
	if str[n] == '0' or str[n] == '1' or str[n] == '2' or str[n] == '3' or str[n] == '4' or str[n] == '5' or str[n] == '6' or str[n] == '7' or str[n] == '8' or str[n] == '9':
		k = k + 1
		break
for n in range(0, len(str)):
	if str[n] == '!' or str[n] == '"' or str[n] == '#' or str[n] == '&' or str[n] == '$' or str[n] == '%' or str[n] == "'" or str[n] == '(' or str[n] == ')' or str[n] == '*' or str[n] == '+' or str[n] == ':':
		k = k + 1
		break
if len(str) >= 8:
	k = k + 1
print(k)
