string_1 = input("Enter 1st string: ")
string_2 = input("Enter 2nd string: ")
is_subset = string_1.count(string_2)
if is_subset == 0:
	print("2nd string is not the subset of 1st")
else:
	print("2nd string is the subset of 1st")

