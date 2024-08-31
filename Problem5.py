import os
with open(os.path.expanduser('~') + '/Desktop/assignment2/inputWithErrors.txt') as f:
    lines= [line.rstrip() for line in f]

fOutput = open(os.path.expanduser('~') + '/Desktop/assignment2/outputClean.txt', 'w')
lines0 = lines[0].title() + '\n' + lines[1].capitalize()    #title and capitalize first line
fOutput.write(lines0 + '\n')    #write first line to output

for i in range(2, len(lines)):
    newline = lines[i].replace(' .', '.').replace(' ,', ',').replace(' )', ')').replace('(', ' (')  #replace errors
    k = newline.find(':')
    newlineFinal = newline[:k+1].title() + newline[k+1:k+3].upper() + newline[k+3:] #correct case before colons

    #to prevent printing "\n" at the end
    if i < len(lines)-1:
        fOutput.write(newlineFinal  + '\n')
    else:
        fOutput.write(newlineFinal)
fOutput.close()

"""Learnings from this code:
1. title() method capitalizes the first letter of each word
2. capitalize() method capitalizes the first letter of the whole line
3. replace() method replaces old string with new string
4. find() method returns the index of the first occurence of the string
5. slicing is used to get the characters between the indices
6. with open() method, we can open a file"""