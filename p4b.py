myStr1 = "In a Democracy, the government is of the people, by the people, and for the people, still people don't go out and vote"
n1 = myStr1.find("people")

myStr2 = myStr1[0:n1] + "PEOPLE" + myStr1[n1+6:]
print(myStr2)

n2 = myStr2.find("people")
myStr3 = myStr2[0:n2] + "pEOPLE" + myStr2[n2+6:]
print(myStr3)

n3 = myStr3.find("people")
myStr4 = myStr3[0:n3] + "pEOPLE" + myStr3[n3+6:]
print(myStr4)

n4 = myStr4.find("people")
myStr5 = myStr4[0:n3] + "peoPLE" + myStr4[n3+6:]
print(myStr5)
