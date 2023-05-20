# https://www.acmicpc.net/problem/9205

from sys import stdin
from collections import deque

def bfs(node):
    q = deque([node])
    while q:
        node = q.popleft()
        for x, y in g:
            nx = abs(node[0] - x)
            ny = abs(node[1] - y)
            if not visit[g.index((x, y))] and nx+ny <= 1000:
                q.append((x, y))
                visit[g.index((x, y))] = 1


tc = int(stdin.readline())

for _ in range(tc):
    n = int(stdin.readline())
    start_x, start_y = map(int, stdin.readline().split())
    visit = [0 for _ in range(n+1)]
    g = []
    for _ in range(n):
        x, y = map(int, stdin.readline().split())
        g.append((x, y))

    arrive_x, arrive_y = map(int, stdin.readline().split())
    g.append((arrive_x, arrive_y))
    bfs((start_x, start_y))
    if visit[-1]: print('happy')
    else: print('sad')