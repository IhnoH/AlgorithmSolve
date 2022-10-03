#https://www.acmicpc.net/problem/5582

import numpy as np

a = 'ABRACADABRA'
b = 'ECADADABRBCRDARA'
lst = list([b])

print(lst)
for i in range(len(b)):
    tmp = np.array([])
    if b[i] not in a:
        for l in lst:
            tmp = [w for w in np.array((np.append(l.split(b[i]), tmp))) if len(w) is not 0]
            #map(lambda i: len(i) is not 0, )

        lst = tmp
        print(lst)

