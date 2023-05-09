from itertools import combinations, product, permutations

t = [1, 2, 3, 4, 5, 6, 7, 8]
k = [[8, 7, 6, 5], [4, 3, 2, 1]]
a = combinations(t, 2)
#print(list(a))
for i, j in a:
    print(i, j)

a = [1, 2, 3, 4]
print(list(permutations(a)))

print(float('inf'))

b = [3, 3, 4]
a.extend(b)
print(a)


def solution(n):
    rev_base = ''

    # 3진법 변환
    while n > 0:
        n, mod = divmod(n, 3)
        rev_base += str(mod)
    print(rev_base)

    res = 0
    t = 1

    for i in rev_base[::-1]:
        res = res + t*int(i)
        t *= 3
    return res
# print(solution(45))