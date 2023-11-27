File = open("input", "r")

total = 0
elfes = []
for line in File.readlines():
    if(line == '\n'):
        elfes.append(total)
        total = 0
        continue

    total += int(line[:-1])

result = 0

elfes.sort()

for i in range(3):
    result += elfes[-1-i]

print(result)