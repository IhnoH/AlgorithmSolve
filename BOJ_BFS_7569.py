# https://www.acmicpc.net/problem/7569

from sys import stdin
from collections import deque

d = [(-1, 0, 0), (0, -1, 0), (1, 0, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]

m, n, h = map(int, stdin.readline().split())
g = [[] for _ in range(h)]
visit = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]
nodes = []

for i in range(h):
    for j in range(n):
        g[i].append(list(map(int, stdin.readline().split())))
        for k in range(m):
                if g[i][j][k] == 1:
                    nodes.append((k, j, i))
                    visit[i][j][k] = 1

def bfs(node):
    q = deque(node)
    result = 0
    while q:
        node = q.popleft()
        day = 1
        for dx, dy, dz in d:
            nx = node[0] + dx
            ny = node[1] + dy
            nz = node[2] + dz
            if -1 < nx < m and -1 < ny < n and -1 < nz < h:
                if not visit[nz][ny][nx]:
                    if g[nz][ny][nx] == 0:
                        visit[nz][ny][nx] = visit[node[2]][node[1]][node[0]] + day
                        q.append((nx, ny, nz))
                        result = 1
                    elif g[nz][ny][nx] == 1:
                        visit[nz][ny][nx] = visit[node[2]][node[1]][node[0]]
                        q.append((nx, ny, nz))
    return result

def ans(result):
    mx = 0
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if visit[i][j][k] == g[i][j][k] == 0: return -1
    if result == 1:
        for i in range(h): mx = max(max(map(max, visit[i])), mx)
        return mx-1

    else: return result


result = bfs(nodes)
print(ans(result))

print(*g, sep='\n', end='\n\n')
print(*visit, sep='\n', end='\n')
