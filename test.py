l = [1, 2, 3]
l.insert(4, 0)
from itertools import permutations
from collections import deque
from sys import stdin

n, m = map(int, stdin.readline().split())

gList = [[0]*(n+1) for _ in range(n+1)]
gMat = [[] for _ in range(n+1)]
visit = [0]*(n+1)

for i in range(m):
    v1, v2 = map(int, stdin.readline().split())
    gList[v1][v2] = gList[v2][v1] = 1
    gMat[v1].append(v2)
    gMat[v2].append(v1)

def bfsMat(node):
    q = deque([node])
    visit[node] = 1
    while q:
        node = q.popleft()
        print(node, end=' ')
        for i in gMat[node]:
            if visit[i]: continue
            q.append(i)
            visit[i] = 1



def bfsList(node):
    q = deque([node])
    visit[node] = 1
    while q:
        node = q.popleft()
        print(node, end=' ')
        for i in range(1, n+1):
            if visit[i] or not gList[node][i]: continue
            print(' | ', end=' ')
            q.append(i)
            visit[i] = 1

def dfs(node):
    visited = []
    needVisit = deque([node])
    while needVisit:
        node = needVisit.pop()
        if node not in visited:
            print(node, end=' ')
            visited.append(node)
            needVisit.extend(gMat[node])


