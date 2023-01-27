# https://www.acmicpc.net/problem/2178
from sys import stdin
from collections import deque

import numpy as np

def bfs(node):
    q = deque([node])
    visit[node[1]][node[0]] = 1
    while q:
        y, x = q.popleft()
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visit[ny][nx] and g[ny][nx]:
                visit[ny][nx] = 1
                q.append((ny, nx))
                g[ny][nx] += g[y][x]


m, n = map(int, stdin.readline().split(' '))
g = [list(map(int, list(stdin.readline()[:n]))) for _ in range(m)]
visit = [[0]*n for _ in range(m)]
d = [(-1, 0), (0, -1), (1, 0), (0, 1)]


bfs((0, 0))
print(g[m-1][n-1])