n = 14#int(input())

def charge(n):
    if n == 0: return -1
    if n%5 == 0: return n//5

    for i in range(n//2+1):
        n2 = (n-(2*i))
        if n2%5 == 0: return i+(n2//5)
    return -1

for i in range(20):
    print(i, charge(i))

