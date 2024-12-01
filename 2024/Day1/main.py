file = open("input", 'r').read().strip()

tabA = []
tabB = []

result = 0

for line in file.split('\n'):
    a = line[0:5]
    b = line[8:]
    
    tabA.append(a)
    tabB.append(b)
    
tabA.sort()
tabB.sort()

for i in range(len(tabA)):
    result += int(tabA[i]) * int(tabB.count(tabA[i]))
    
print(result)