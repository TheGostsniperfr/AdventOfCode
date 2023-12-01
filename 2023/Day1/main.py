file = open("input", 'r')

#Part 1

total = 0
for line in file:
    firstDigit = None
    lastDigit = None
    for char in line:
        if char.isdigit():
            current_val = int(char)
            if firstDigit is None:
                firstDigit = current_val
            lastDigit = current_val
    if(firstDigit != None):
        total += firstDigit * 10 + lastDigit


print("Part 1 Result :", total)


#Part 2 :
file.seek(0)

convertNb = ["one","two","three","four","five","six","seven","eight","nine"]

total = 0
firstWord = None
lastWord = None

for line in file.readlines():
    for letter_i in range(len(line)):
        
        letter = line[letter_i] 
        if(letter.isdigit()):
            if(firstWord == None):
                firstWord = int(letter)
            lastWord = int(letter)
        else:
            for nb, val in enumerate(convertNb):
                if(line[letter_i:].startswith(val)):
                    if(firstWord == None):
                        firstWord = nb+1
                    lastWord = nb+1
                
    if(firstWord != None):
        total += firstWord * 10 + lastWord
        #print(f"word find : {firstWord} | {lastWord}")
        
        
    firstWord = None
    lastWord = None
    
    
print("Part 2 Result :", total)      
file.close()