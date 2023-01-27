# https://www.acmicpc.net/problem/7576
from sys import stdin
from collections import deque

import numpy as np

def bfs(q):
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < m and 0 <= ny < n and not g[nx][ny]:
                g[nx][ny] = g[x][y] + 1
                q.append((nx, ny))

def solution():
    q = deque()
    for i in range(m):
        for j in range(n):
            if g[i][j] == 1: q.append((i, j))

    day = 0
    bfs(q)
    for i in range(m):
        for j in range(n):
            if g[i][j] == 0: return -1
        day = max(day, max(g[i]))
    return (day - 1)


n, m = map(int, stdin.readline().split(' '))
g = [list(map(int, stdin.readline().split(' '))) for _ in range(m)]
d = [(-1, 0), (0, -1), (0, 1), (1, 0)]

print(solution())

