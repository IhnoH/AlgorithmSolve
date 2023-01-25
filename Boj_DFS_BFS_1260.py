# https://www.acmicpc.net/problem/1260
from collections import deque

num, rlat, node = map(int, input().split(' '))

g = [[0]*(num+1) for _ in range(num+1)]

for i in range(rlat):
    f1, f2 = map(int, input().split(' '))
    g[f1][f2] = g[f2][f1] = 1

visit = [0]*(num+1)

def dfs(node):
    print(node, end=' ')
    visit[node] = 1
    for i in range(1, num+1):
        if visit[i] or g[node][i] == 0: continue
        dfs(i)

def bfs(node):
    q = deque([node])
    visit[node] = 0
    while q:
        node = q.popleft()
        print(node, end=' ')
        for i in range(1, num+1):
            if not visit[i] or not g[node][i]: continue
            q.append(i)
            visit[i] = 0

dfs(node)
print()
bfs(node)