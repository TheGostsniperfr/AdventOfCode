import re

file = open("input", 'r').read().strip()

resultP1 = 0

for line in file.split('\n'):
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, line)
    
    for l, r in matches:
        print(l + " * " + r)

        resultP1 += int(l) * int(r)


enabled = True
resultP2 = 0

tokens = re.finditer(r"(do\(\)|don't\(\)|mul\((\d+),(\d+)\))", file)

for match in tokens:
    token = match.group(0)

    if (token) == "do()":
        enabled = True 
    elif (token) == "don't()":
        enabled = False
    else:
        if (enabled):
            l, r = int(match.group(2)), int(match.group(3))
            resultP2 += l * r

print(resultP1)
print(resultP2)
