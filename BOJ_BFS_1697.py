# https://www.acmicpc.net/problem/1697

from sys import stdin
from collections import deque

d = [-1, 1, 2]
def bfs(n):
    if n == k: return 0
    q = deque([n])
    while q:
        node = q.popleft()
        for i in d:
            if i == 2: dn = node*i
            else: dn = node + i
            if 0 <= dn <= 100000 and not sec[dn]:
                if dn != k:
                    q.append(dn)
                    sec[dn] = sec[node]+1
                else: return sec[node]+1

n, k = map(int, stdin.readline().split())
mx = max(n, k)
sec = [0 for _ in range(100001)]
print(bfs(n))

