from sys import stdin
from collections import deque

d = [(0, -1), (-1, 0), (0, 1), (1, 0)]

def bfs(node, h):
    q = deque([node])
    visit[node[0]][node[1]] = 1
    while q:
        node = q.popleft()
        for dx, dy in d:
            nx = node[0] + dx
            ny = node[1] + dy
            if 0 <= nx < n and 0 <= ny < n:
                if not visit[nx][ny] and g[nx][ny] > h:

                    visit[nx][ny] = 1
                    q.append((nx, ny))



n = int(stdin.readline())
g = []

for _ in range(n):
    g.append(list(map(int, stdin.readline().split())))

mx = max(list(map(max, g)))
result = []
v = [[0]*(n+1) for _ in range(n+1)]

for h in range(mx):
    visit = [[0] * (n + 1) for _ in range(n + 1)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visit[i][j] and g[i][j] > h:
                bfs((i, j), h)
                cnt += 1

    # print(h)
    # print(*visit, sep='\n', end='\n\n')
    result.append(cnt)

print(result, max(result))

