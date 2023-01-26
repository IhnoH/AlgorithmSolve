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