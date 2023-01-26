from sys import stdin
from collections import deque
def bfs(node):
    q = deque([node])
    visit[node[0]][node[1]] = 1

    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < m and 0 <= ny < n and not visit[nx][ny] and g[nx][ny]:
                q.append((nx, ny))
                visit[nx][ny] = 1

d = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
nIsland = []

while 1:
    n, m = map(int, stdin.readline().split(' '))
    if n == m == 0: break
    g = []
    for _ in range(m):
        g.append(list(map(int, stdin.readline().split(' '))))


    visit = [[0]*n for _ in range(m)]
    cnt = 0
    for i in range(m):
        for j in range(n):
            if not visit[i][j] and g[i][j]:
                bfs((i, j))
                #print()
                cnt += 1

    nIsland.append(cnt)

for i in nIsland: print(i)