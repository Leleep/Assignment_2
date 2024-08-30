myString = input("Write a string: ") #Asks for string as an input

ind = int(input("Enter the index of position: ")) #Asks for index

rtdstrng = myString[ind:len(myString)+1] + myString[0:ind] 

"""Slices the original string from the given index upto the end and then 
    concatenates the remaining string so as to rotate the string about the given index"""

print(rtdstrng)