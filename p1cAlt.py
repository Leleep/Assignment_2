swv = input("Enter a string: ")
for i in range(len(swv)):
	if (swv[i].lower() == "a" or swv[i].lower() =="e" or swv[i].lower() =="i" or swv[i].lower() =="o" or swv[i].lower() =="u"):
		swv = swv[:i] + "?" + swv[i+1:]

print(swv)