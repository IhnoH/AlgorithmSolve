# https://www.acmicpc.net/problem/1707
from sys import stdin
from collections import deque

def bfs(node):
    q = deque([node])
    visit[node] = 1
    while q:
        node = q.popleft()
        for i in g[node]:
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
    visit[0] = 1
    g = [[] for _ in range(n+1)]
    node = 0
    for _ in range(m):
        v1, v2 = map(int, stdin.readline().split())
        g[v1].append(v2)
        g[v2].append(v1)
        node = v1
    ans = True

    while 0 in visit:
        node = visit.index(0)
        if not bfs(node):
            ans = False
            break
    if ans: print('YES')
    else: print('NO')

