file = open("input", 'r').read().strip()

total = 0


L = file.split('\n')

timeStr,distanceStr = file.split('\n')

times = []
dist = []

"""part 1
for i in timeStr.split(":")[-1].split():
    times.append(int(i))
    
    
for i in distanceStr.split(":")[-1].split():
    dist.append(int(i))
"""

#part 2

for i in timeStr.split(":")[-1].replace(" ", "").split():
    times.append(int(i))
    
    
for i in distanceStr.split(":")[-1].replace(" ", "").split():
    dist.append(int(i))

for i in range(len(times)):
    cT = times[i]
    cD = dist[i]
    timeL= []

    tmpV = 0
    
    for tmpV in range(cT):
        newD = (cT-tmpV) * tmpV
        #print(tmpV, "current distance : ",newD, "hold", tmpV, "remain", cT - tmpV)       
        
        if(newD> cD):
            timeL.append(tmpV)
        
        #print(timeL)
        
    if(total == 0):
        total = len(timeL)
    else:
        total *= len(timeL)
        
    

print("Part 1 or 2 Result :", total)