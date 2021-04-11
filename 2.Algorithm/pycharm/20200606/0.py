target = input()
level = 0
if len(target) >= 10:
	level += 1
check = [0] * 4
tc = set(target)
for t in tc:
	code = ord(t)
	if 48 <= code < 58:
		check[0] = 1
	elif 65 <= code < 91:
		check[1] = 1
	elif 97 <= code < 123:
		check[2] = 1
	else:
		check[3] = 1
level += sum(check)
print(f'LEVEL{level}')