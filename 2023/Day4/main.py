file = open("input", 'r').read().strip()

total = 0
total2 = 0

dataList = []


for line in file.split('\n'):
    gameId, data = line.split(":")
    gameId = int(gameId.split()[-1])
    
    trueC, card = data.split("|")
    
    trueC = trueC.split()
    card = card.split()
    
    scoreG = 0
    start = False
    
    #gameId -> dataList[gameId-1]
    if(len(dataList) < gameId):
        dataList.append(1)
    else:
        dataList[gameId-1] += 1
    
    
    nbFound = 0
    for i in trueC:
        if(i in card):
            nbFound += 1
            if(start == False):
                scoreG = 1
                start = True
            else:
                scoreG  *= 2   
                
    for i in range(nbFound):
        if(len(dataList) < gameId+1 + i):
            dataList.append(0)
        
        dataList[gameId-1 +1 + i] += dataList[gameId-1] 
                
    #print(scoreG)
    total += scoreG    

print("Part 1 Result :", total)
print("Part 2 Result :", sum(dataList))