InputStr = input("Enter a string: ")
InputChar = input ("Enter a character: ")
inputstr = InputStr.lower()
inputchar = InputChar.lower()
n = 0
for i in range(len(InputStr)):
	if inputstr[i] == inputchar:
		n += 1
if n != 0:
	fidx = inputstr.find(inputchar)
	lidx = inputstr.rfind(inputchar)
	print("First index is", fidx)
	print("Last index is", lidx)
else:
	print(-1)
print("Total occurences of InputChar:", n)
