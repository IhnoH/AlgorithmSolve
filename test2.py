from itertools import combinations, product

t = [1, 2, 3, 4, 5, 6, 7, 8]
k = [[8, 7, 6, 5], [4, 3, 2, 1]]
a = combinations(t, 2)
#print(list(a))
for i, j in a:
    print(i, j)
