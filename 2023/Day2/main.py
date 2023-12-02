file = open("input", 'r').read().strip()

total = 0
total2 = 0

for line in file.split('\n'):
    gameId, rightLine = line.split(":")
    l = [0,0,0]
    pb = False
    for subGame in rightLine.split(";"):
        for item in subGame.split(","):
            nb, color = item.split()
            val = int(nb)
            if(color == "red"):
                l[0] = max(val, l[0])
                if(val > 12):
                    pb = True
            elif(color == "green"):
                l[1] = max(val, l[1])
                if(val > 13):
                    pb = True
            elif(color == "blue"):
                l[2] = max(val, l[2])
                if(val > 14):
                    pb = True

    if(not pb):
        total += int(gameId.split()[-1])
    total2 += l[0]*l[1]*l[2]

print("Part 1 Result :", total)
print("Part 2 Result :", total2)