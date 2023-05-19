# https://www.acmicpc.net/problem/13549

from sys import stdin
from collections import deque

d = [2, -1, 1]
def bfs(node):
    if n == k: return 0
    q = deque([node])
    visit[node] = 1
    while q:
        x = q.popleft()
        for i in d:
            if i == 2:
                nx = x*2
                t = 0
            else:
                nx = x + i
                t = 1
            if -1 < nx < 100001 and not visit[nx]:
                q.append(nx)
                visit[nx] = visit[x] + t
                if nx == k: return visit[nx]-1

visit = [0 for _ in range(100001)]
n, k = map(int, stdin.readline().split())
print(bfs(n))