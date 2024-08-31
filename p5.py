import os
with open(os.path.expanduser('~') + '/folder1/inputWithErrors.txt') as f:
    lines= [line.rstrip() for line in f]
# print(lines[0].title())
# for i in range(1,9):
#         print(lines[i][:1].upper()+lines[i][1:].lower())

fOutput = open(os.path.expanduser('~') + '/folder1/outputClean.txt', 'w')
for line in lines:
    newline = line.replace(' .', '.')
    newline2 = newline.replace(' ,', ',')
    newline3 = newline2.replace(' )', ')')
    newline4 = newline3.replace('(', ' (')
#to correct case of title, use firstIter = True flag, as discussed in class
    k = newline4.find(':')
    newlineFinal = newline4[:k+1].title() + newline4[k+1:k+3].upper() + newline4[k+3:]
#to correct case for start of each line find full stop and use slicing
#to correct 4c., replace '(' with ' (', then think & perform one more replace 
#save final output in newlineFinal
    fOutput.write(newlineFinal  + '\n')
fOutput.close()
