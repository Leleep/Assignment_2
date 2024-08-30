inputstr = input("Enter a string: ").lower()
inputchar = input("Enter a char: ").lower()

n = 0
lfi = []

for i in range(len(inputstr)):
	if inputstr[i] == inputchar:
		n += 1
		lfi.append(i)

print("Total number of occurences of InputChar is", n)


if n != 0:
	print("First index is", lfi[0], "\nLast index is", lfi[n-1])
else:
	print(-1)
