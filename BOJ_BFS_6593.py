# https://www.acmicpc.net/problem/6593

from sys import stdin
from collections import deque

ans = []
d = [(-1, 0, 0), (0, -1, 0), (1, 0, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]

def bfs(node):
    q = deque([node])
    visit[node[2]][node[1]][node[0]] = 1
    while q:
        n = q.popleft()
        for nx, ny, nz in d:
            dx = n[0] + nx
            dy = n[1] + ny
            dz = n[2] + nz
            if -1< dx <a and -1< dy <b and -1< dz <c:
                if not visit[dz][dy][dx] and g[dz][dy][dx] == '.':
                    q.append((dx, dy, dz))
                    visit[dz][dy][dx] = visit[n[2]][n[1]][n[0]] + 1
                elif g[dz][dy][dx] == 'E':
                    return visit[n[2]][n[1]][n[0]]
    return None

while 1:
    c, b, a = map(int, stdin.readline().split())
    if c == a == b == 0: break;
    visit = [[[0 for _ in range(a)] for _ in range(b)] for _ in range(c)]
    g = [[] for _ in range(c)]
    start = ()
    arrive = ()
    for i in range(c):
        for j in range(b+1):
            tmp = stdin.readline()
            if tmp == '\n': continue
            g[i].append(tmp[:-1])
            if 'S' in tmp: start = (tmp.index('S'), j, i)
            if 'E' in tmp: arrive = (tmp.index('E'), j, i)
    
    ans.append(bfs(start))

for i in ans:
    if i == None: print('Trapped!')
    else: print(f'Escaped in {i} minute(s).')
