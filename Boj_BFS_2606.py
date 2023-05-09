from sys import stdin
from collections import deque

def bfs(node):
    q = deque([node])
    visit[node] = 1
    virus = 0
    while q:
        node = q.popleft()
        for i in g[node]:
            if not visit[i]:
                q.append(i)
                virus += 1
                visit[i] = 1
    return virus

n = int(stdin.readline())
m = int(stdin.readline())
visit = [0]*(n+1)

g = [[] for _ in range(n+1)]

for i in range(m):
    v1, v2 = map(int, stdin.readline().split())
    g[v1].append(v2)
    g[v2].append(v1)


print(bfs(1))

