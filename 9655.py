n = 5#int(input())

def oneThr(n):
    i = 0
    sw = [1, 3]
    tmp = n%4
    if tmp == 0: return 'CY'
    while True:
        if tmp - 1 == 0: return 'CY'
        elif tmp - 3 == 0: return 'SK'
        else: tmp = tmp - 1*sw[i%2]
        i += 1

print(oneThr(n))