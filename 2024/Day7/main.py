import sys
import re
from itertools import product

file = open("input", 'r').read().strip()
sys.setrecursionlimit(10**5)
def p(str: str):
    print(str)

resultP1 = 0
resultP2 = 0

STEP = "PARSE"

TESTS = []

for line in file.split('\n'):
    match (STEP):
        case "PARSE":
            tmp = []
            vals = line.split(':')
            
            parseVals = vals[1].split()
            for i in parseVals:
                tmp.append(int(i))
            
            TESTS.append([int(vals[0]), tmp])


def check(result, vals, concat):
    if (len(vals) == 1):
        return result == vals[0]
    
    if (check(result, [vals[0] + vals[1]] + vals[2:], concat)):
        return True
    
    if (check(result, [vals[0] * vals[1]] + vals[2:], concat)):
        return True
    
    if (concat and check(result, [int(str(vals[0]) + str(vals[1]))] + vals[2:], concat)):
        return True

for i in TESTS:
    if (check(i[0], i[1], False)):
        resultP1 += i[0]
        
    if (check(i[0], i[1], True)):
        resultP2 += i[0] 
        
p(resultP1)
p(resultP2)
