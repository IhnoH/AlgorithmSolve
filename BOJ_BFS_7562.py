# https://www.acmicpc.net/problem/7562

from sys import stdin
from collections import deque

d = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, 1), (2, -1)]

tc = int(stdin.readline())

def bfs(node):
    if start == arrive: return 0
    q = deque([node])
    visit[node[1]][node[0]] = 1
    while q:
        node = q.popleft()
        for dx, dy in d:
            nx = node[0] + dx
            ny = node[1] + dy
            if -1 < nx < n and -1 < ny < n:
                if not visit[ny][nx]:
                    if nx == arrive[0] and ny == arrive[1]:
                        a = visit[node[1]][node[0]]
                        return a
                    else:
                        visit[ny][nx] = visit[node[1]][node[0]] + 1
                        q.append((nx, ny))

ans = []
for _ in range(tc):
    n = int(stdin.readline())
    start = list(map(int, stdin.readline().split()))
    arrive = list(map(int, stdin.readline().split()))
    visit = [[0 for _ in range(n)] for _ in range(n)]

    ans.append(bfs(start))

for i in ans: print(i)