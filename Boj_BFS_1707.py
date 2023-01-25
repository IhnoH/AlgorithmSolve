# https://www.acmicpc.net/problem/1707
from sys import stdin
from collections import deque

def bfs(node):
    q = deque([node])
    visit[node] = 1
    while q:
        node = q.popleft()
        for i in range(1, n+1):
            if g[node][i]:
                if not visit[i]:
                    q.append(i)
                    if visit[node] == 1: visit[i] = 2
                    elif visit[node] == 2: visit[i] = 1
                elif visit[i] == visit[node]: return False
    return True


tc = int(stdin.readline())

for t in range(tc):
    n, m = map(int, stdin.readline().split())
    visit = [0]*(n+1)
    g = [[0]*(n+1) for _ in range(n+1)]
    node = 0
    for _ in range(m):
        v1, v2 = map(int, stdin.readline().split())
        g[v1][v2] = g[v2][v1] = 1
        node = v1
    if bfs(node): print('YES')
    else: print('NO')

