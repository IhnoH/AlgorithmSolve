# https://www.acmicpc.net/problem/2667
from collections import deque
from sys import stdin

def bfs(node):
    q = deque([node])
    visit[node[0]][node[1]] = 1
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny] and g[nx][ny]:
                q.append((nx, ny))
                visit[nx][ny] = 1
                cnt += 1
    return cnt


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(stdin.readline())
visit = [[0]*n for _ in range(n)]
g = []
for i in range(1, n+1):
    s = stdin.readline()
    s = s[:n]
    g.append(list(map(int, list(s))))

house = []
for i in range(n):
    for j in range(n):
        if not visit[i][j] and g[i][j]:
            house.append(bfs((i, j)))

house.sort()
print(len(house))
for i in house: print(i)