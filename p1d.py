smpstr = input("Enter a string to check if it's a palindrome: ")
if (smpstr == smpstr[::-1]):
	print("This string is a palindrome")
else:
	print("This string is not a palindorme")
