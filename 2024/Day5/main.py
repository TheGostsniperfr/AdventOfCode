import sys
import re

file = open("input", 'r').read().strip()
sys.setrecursionlimit(10**8)
def p(str: str):
    print(str)

resultP1 = 0
resultP2 = 0

STEP = "RULES"

rules = {}
pages = []

for line in file.split('\n'):
    match (STEP):
        case "RULES":
            if (line == ""):
                STEP = "PAGES"
                continue
            
            val = line.split('|')
            l, r = int(val[0]), int(val[1])
            
            if (not l in rules):
                rules[l] = [r]
            else:
                rules[l].append(r)
        
        case "PAGES":
            tmp = []
            for val in line.split(','):
                tmp.append(int(val))
            
            pages.append(tmp)
        
        
for i in rules.keys():
    p(f'{i}: {rules[i]}')
    
p("\n\n")
        
def checkRules(l, r):
    if (l in rules):
        if (not r in rules[l]):
            return False
        
    if (r in rules):
        if (l in rules[r]):
            return False
        
    return True

def checkP1(page):
    for i in range(0, len(page) - 1):  
        if (not checkRules(page[i], page[i+1])):
            return False
             
    return True

def checkP2(page):
    for i in range(len(page) - 1):
        for j in range(i + 1, len(page)):
            if (not checkRules(page[i], page[j])):
                page[i], page[j] = page[j], page[i]

for page in pages:
    if (checkP1(page)):
        resultP1 += page[len(page) // 2]
    else:
        checkP2(page)
        resultP2 += page[len(page) // 2]


    
p(resultP1)
p(resultP2)