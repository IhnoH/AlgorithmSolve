# https://www.acmicpc.net/problem/11724
from collections import deque
from sys import stdin

num, m = map(int, stdin.readline().split())

g = [[0]*(num+1) for _ in range(num+1)]

for i in range(m):
    v1, v2 = map(int, stdin.readline().split())
    g[v1][v2] = g[v2][v1] = 1

visit = [0]*(num+1)
visit[0] = 1
cc = 0

def bfs(node):
    q = deque([node])
    visit[node] = 1
    while q:
        node = q.popleft()
        for i in range(1, num+1):
            if visit[i] or not g[node][i]: continue
            q.append(i)
            visit[i] = 1


def dfs(node):
    visit[node] = 1
    for i in range(1, num+1):
        if visit[i] or not g[node][i]: continue
        bfs(i)


while 0 in visit:
    node = visit.index(0)
    dfs(node)
    cc += 1


print(cc)