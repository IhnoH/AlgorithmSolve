from collections import deque

n, m = map(int, input().split(' '))

maze = []

for i in range(n): maze.append(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False]*(m) for i in range(n)]
alive = {'o':0, 'v':0}
area = {'o': 0, 'v': 0}
queue = deque([(0, 0)])
visited[0][0] = True
notSum = False
while queue:
    x, y = queue.popleft()
    if maze[x][y] != '.' and maze[x][y] != '#': area[maze[x][y]] += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if not visited[nx][ny] and maze[nx][ny] != '#':
                if nx == n or nx == 0 or ny == m or ny == 0:
                    notSum = True
                queue.append((nx, ny))
                visited[nx][ny] = True

    if not queue:
        if area['v'] >= area['o'] and notSum:
            alive['v'] += area['v']
            notSum = False
        elif area['v'] < area['o'] and notSum:
            alive['o'] += area['o']
            notSum = False
        area['o'] = area['v'] = 0

        for i in range(1, n-1):
            o = maze[i].find('o')
            v = maze[i].find('v')
            if o != -1 and 0 < o < m-1:
                if visited[i][o] == False:
                    queue.append((i, o))
                    visited[i][o] = True
                    break
            if v != -1 and 0 < v < m-1:
                if visited[i][v] == False:
                    queue.append((i, v))
                    visited[i][v] = True
                    break



print(alive['o'], alive['v'])

