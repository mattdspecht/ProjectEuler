import math

def findSolutions(n: int):
    ret = 0
    for i in range(n//2):
        for j in range(n-i):
            if((n-i-j)**2 == i**2 + j**2):
                ret+=0.5
    return math.floor(ret)

best = 0
retVal = 0
for i in range(1000):
    if(findSolutions(i) > best):
        best = findSolutions(i)
        retVal = i
print(retVal)