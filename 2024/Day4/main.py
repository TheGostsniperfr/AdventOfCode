file = open("input", 'r').read().strip()

tab = []

resultP1 = 0
resultP2 = 0

for line in file.split('\n'):
    tmp = []
    for i in line:
       tmp.append(i)
    tab.append(tmp)


W = "XMAS"
axes = [ [0, 1], [ 0, -1 ], [ 1, 0 ], [ -1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]


def getVal(x, y):
    if (x < 0 or y < 0 or x >= len(tab[0]) or y >= len(tab)):
        return None
    
    return tab[y][x]

# print(getVal(0, 0))

def check(x, y):

    global resultP1    
    for aX, aY in axes:
        isGood = True

        for time in range(0, len(W)):
            val = getVal(time * aX + x, time * aY + y)
            # print(val)
            # print(W[time])
            if (val == None or val != W[time]):
                isGood = False
                # print("test")
                break
            # else:
                # print("ok")
        
        if (isGood):
            resultP1 += 1

def checkP2(x, y):
    global resultP2
    if (1<=x<len(tab[y]) - 1 and 1<=y<len(tab) - 1 and getVal(x, y) == 'A'):
    
        x1 = getVal(x - 1, y - 1)
        x2 = getVal(x + 1, y - 1)
        x3 = getVal(x - 1, y + 1)
        x4 = getVal(x + 1, y + 1)
        
        if ((x1 == 'M' and x4 == 'S') or (x4== 'M' and x1 == 'S')):
            if ((x2 == 'M' and x3 == 'S') or (x3 == 'M' and x2 == 'S')):
                resultP2 += 1
    

for y in range(len(tab)):
    for x in range(len(tab[y])):
        check(x, y)
        checkP2(x, y)
            
print(resultP1)   
print(resultP2)   