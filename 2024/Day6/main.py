import sys
import re

file = open("input", 'r').read().strip()
sys.setrecursionlimit(10**8)
def p(str: str):
    print(str)

resultP1 = 0
resultP2 = 0

STEP = "MAP"

map = []

for line in file.split('\n'):
    match (STEP):
        case "MAP":
            tmp = []
            for i in line:
                tmp.append(i)
            map.append(tmp)
                    
H = len(map)
W = len(map[0])

for i in range(H):
    for j in range(W):
        if (map[i][j] == '^'):
            Y_start, X_start = i, j

# print((X, Y))

def run (X_start, Y_start):
    global resultP1
    # 0 UP | 1 RIGHT | 2 DOWN | 3 LEFT (MOD 4)
    D = 0 
    
    u = 0
    
    X, Y = X_start, Y_start
    PATH = set()
    PATH.add((X, Y))
    
    PATH_D = set()
    PATH_D.add((X, Y, D))

    while (True):
        new_X = X
        new_Y = Y
        if (D == 0):
            new_Y = Y - 1
        elif (D == 1):
            new_X = X + 1
        elif (D == 2):
            new_Y = Y + 1
        else:
            new_X = X - 1
        
        if (not (0<=new_X<W and 0<=new_Y<H)):
            resultP1 = len(PATH)
            break
        
        

        
        if (map[new_Y][new_X] == '#'):
            D = (D+1)%4
            
        else:
            X = new_X
            Y = new_Y
            # p(f'{u}: ({X}, {Y})')
            u+= 1
            PATH.add((X, Y))
            
            if ((X, Y, D) in PATH_D):
                return False
            
            PATH_D.add((X, Y, D))
    
    return True
        

# print("\n\n")
# for i in range(W):
#     tmp = []
#     for j in range(H):        
#         if ((i, j) in PATH):
#             tmp.append('O')

#         else:
#             tmp.append(map[j][i])
#     p(tmp)

run(X_start, Y_start)
p(resultP1)

for i in range(W):
    for j in range(H):
        if (map[j][i] == "#" or (j == Y_start and i == X_start)):
            continue
        
        map[j][i] = "#"
        if (not run(X_start, Y_start)):
            resultP2 += 1
            
        map[j][i] = "."
        
p(resultP2)
            
    