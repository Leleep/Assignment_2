import os
with open(os.path.expanduser('~') + '/folder1/inputWithErrors.txt') as f:
    lines= [line.rstrip() for line in f]
print(lines[0].title())
