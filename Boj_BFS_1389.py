from collections import deque

num, rlat = map(int, input().split(' '))

g = [[0]*(num+1) for _ in range(num+1)]

for i in range(rlat):
    f1, f2 = map(int, input().split(' '))
    g[f1][f2] = g[f2][f1] = g[f1][f1] = g[f2][f2] = 1


min = 100000
answer = 0
for i in range(num, 0, -1):
    queue = deque([i])
    visited = [False]*(num+1)
    visited[i] = True
    dist = [0 for _ in range(len(g[0]))]
    while queue:
        node = queue.popleft()
        #print(node)
        for n in range(len(g[node])):
            if not visited[n] and g[node][n] == 1 and node != n and n != 0:
                dist[n] = dist[node]+1
                queue.append(n)
                visited[n] = True
    d = sum(dist)
    if d <= min:
        min = d
        answer = i
    #print(end='\n\n')
print(answer)
