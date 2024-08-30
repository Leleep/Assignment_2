#input two strings of same length
str1 = input("Enter 1st string: ")
str2 = input("Enter 2nd string of same length as 1st string: ")

#Create an empty string

AnsStr = ""
for i in range(0, len(str1), 2):
	if str1[i] == str2[i]:
		AnsStr = AnsStr + str1[i]
print(AnsStr)
