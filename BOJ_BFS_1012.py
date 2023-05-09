# https://www.acmicpc.net/problem/1012

from sys import stdin
from collections import deque

d = [(0, -1), (-1, 0), (0, 1), (1, 0)]
def bfs(node):
    q = deque([node])
    visit[node[0]][node[1]] = 1
    while q:
        y, x = q.popleft()
        for dx, dy in d:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m:
                if not visit[ny][nx] and g[ny][nx]:
                    visit[ny][nx] = 1
                    q.append((ny, nx))

tc = int(stdin.readline())

result = []
for c in range(tc):
    n, m, t = map(int, stdin.readline().split())
    nods = []
    visit = [[0] * n for _ in range(m)]
    g = [[0] * n for _ in range(m)]

    for _ in range(t):
        x, y = map(int, stdin.readline().split())
        g[y][x] = 1
        nods.append((y, x))

    ans = 0

    for nod in nods:
        if not visit[nod[0]][nod[1]] and g[nod[0]][nod[1]]:
            bfs(nod)
            ans += 1
    result.append(ans)

for i in result: print(i)