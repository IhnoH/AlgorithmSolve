stroke = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

a = 'CJM'
b = 'HER'
sumList = []
for i in range(len(a)):
    sumList.append(stroke[ord(a[i]) - 65])
    sumList.append(stroke[ord(b[i]) - 65])

def sumStroke(l):
    if len(l) == 2: return l
    retL = []
    print(l)
    for i in range(len(l)-1):
        retL.append((l[i]+l[i+1])%10)
    return sumStroke(retL)

result = sumStroke(sumList)
print(str(result[0])+str(result[1]))
