file = open("input", 'r').read().strip()

total = 0
total2 = 0

symboleMap = []


def getNbInLine(x, y) -> int:
    currentNb = 0
    valid = False

    l = []

    for i in range(len(symboleMap[y])):
        val = symboleMap[y][i]
        if(val.isdigit()):
            if(i >= x-1 and i <= x+1):
                valid = True
            currentNb  = currentNb * 10 + int(val)
            l.append(i)

        else:
            if(valid):
                #clean
                for i in l:
                    symboleMap[y][i] = '.'
                return currentNb
            else:
                l = []
                currentNb = 0

    #check last

    #clean
    for i in l:
       symboleMap[y][i] = '.'
    return currentNb



direction = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

def getSumAdj(x, y):
    global total
    global total2

    sum1 = 0
    sum2 = 0

    for xD,yD in direction:
        newX = xD + x
        newY = yD + y

        if(newX >= 0 and newX < len(symboleMap[0]) and newY >= 0 and newY < len(symboleMap)):
            if(symboleMap[newY][newX].isdigit()):
                tmp = symboleMap[newY].copy()

                total += getNbInLine(newX, newY)

                #part2
                if(symboleMap[y][x] == '*'):
                    symboleMap[newY] = tmp
                    if(sum1 == 0):
                        val = getNbInLine(newX, newY)
                        sum1 = val
                        #print(val)
                    else:
                        val = getNbInLine(newX, newY)
                        sum2 = val
                        #print(val)

    total2 += sum1*sum2


#main (#what a ugly code :/)
for line in file.split('\n'):
    lineMap = []

    for c in line:
        lineMap.append(c)

    symboleMap.append(lineMap)

for y in range(len(symboleMap)):
    for x in range(len(symboleMap[y])):
        val = symboleMap[y][x]
        if(not val.isdigit() and val != '.'):
            getSumAdj(x,y)


print("Part 1 Result :", total)
print("Part 2 Result :", total2)