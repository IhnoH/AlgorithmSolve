
l = [
[[5, 4, 3, 4, 5], [4, 3, 2, 3, 4], [5, 4, 3, 4, 5]],
[[4, 3, 2, 3, 4], [3, 2, 1, 2, 3], [4, 3, 2, 3, 4]]
]
mx = 0
i = [(4, 3), (2, 1)]
print(i.index((2, 1)))
for i in range(2):
    mx = max(max(map(max, l[i])), mx)

    print(mx)

