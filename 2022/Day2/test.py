rule = {'X': 1, 'Y': 2, 'Z':3, 'A': 1, 'B': 2, 'C':3 }

looser = {'A':'Z', 'B': 'X', 'C': 'Y'}
winner = {'A':'Y', 'B': 'Z', 'C': 'X'}

file = open("input", 'r')

elfScore = 0
yourScore = 0

winScore = 6
drawScore = 3

for line in file.readlines():
    elf = line[0]
    you = line[2]

    if(you == 'X'):
        you = looser[elf]
    elif(you == 'Y'):
        you = elf
    else:
        you = winner[elf]

    if(elf == 'A' and you == 'Z'):
        elfScore += winScore
    elif(elf == 'B' and you == 'X'):
        elfScore += winScore
    elif(elf == 'C' and you == 'Y'):
        elfScore += winScore
    elif(rule[elf] == rule[you]):
        elfScore += drawScore
        yourScore += drawScore

    else:
        yourScore += winScore

    elfScore += rule[elf]
    yourScore += rule[you]

print(yourScore)