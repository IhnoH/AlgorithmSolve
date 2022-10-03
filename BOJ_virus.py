k = int(input())
n = int(input())
graph = {}

for i in range(n):
    tmp = input().split(' ')
    graph[tmp[0]].update(tmp[1])

print(graph)

def bfs(v):
    visited = [v]
    que = [v]
    while que:
        v = que.pop(0)
        #for i in gr

def solution():
    pass
