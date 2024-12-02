file = open("input", 'r').read().strip()

tabA = []

resultP1 = 0
resultP2 = 0

for line in file.split('\n'):
    tmp = []
    for val in line.split(' '):
        tmp.append(int(val))
        
    tabA.append(tmp)
    
def checkTab(tab):
    if (not (tab == sorted(tab) or tab == sorted(tab, reverse=True))):
        return False
    
    last = tab[0]
    for i in range(1, len(tab)):
        d = abs(last - tab[i]) 
        last = tab[i]
        if (d > 3 or d < 1):
            return False
    
    return True
        
for tab in tabA:
    if (checkTab(tab)):
        resultP1 += 1   
    check = False
    for i in range(len(tab)):
        subTab = tab[:i] + tab[i+1:]
        if (checkTab(subTab)):
            check = True
        
    if (check):
        resultP2 += 1
        
            
print(resultP1)   
print(resultP2)   