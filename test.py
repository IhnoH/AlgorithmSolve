l = [1, 2, 3]
l.insert(4, 0)

from collections import deque


def bfs(graph, input_start):
    visited = [False] * len(graph)
    answer = []
    queue = deque()
    queue.append(input_start)
    visited[input_start] = True

    while queue:
        node = queue.popleft()
        answer.append(node)
        for i in range(len(graph[node])):
            print(node, end=" ")
            if graph[node][i] == 1 and not visited[i] and node != i:
                print(i)
                queue.append(i)
                visited[i] = True
        return answer


def bfs2(graph, start, visited):
    queue = deque()
    queue.append(start)
    while queue:
        value = queue.popleft()
        if not visited[value]:
            print(value, end=' ')
            visited[value] = True
            for c in range(len(graph[value])):
                if graph[value][c] == 1 and not visited[c]:
                    queue.append(c)

def bfs3(graph, visited):
    queue = deque([1])
    distance = [0 for _ in range(len(graph[0]))]
    while queue:
        node = queue.popleft()
        print(node)
        for i in range(1, len(graph[node])):
            if not visited[i] and graph[node][i] == 1 and node != i and i != 0:
                visited[i] = True
                distance[i] = distance[node]+1
                queue.append(i)
    print(distance)


graph = [[0, 0, 0, 0, 0, 0],
     [0, 1, 0, 1, 1, 0],
     [0, 0, 1, 1, 0, 0],
     [0, 1, 1, 1, 1, 0],
     [0, 1, 0, 1, 1, 1],
     [0, 0, 0, 0, 1, 1]]

visited = [False] * (len(graph[0]))

start = 0

#print('bfs 결과:', bfs(graph, start))
#print('bfs 결과:', bfs2(graph, start, visited))
print(bfs3(graph, visited))

t= [[1, 2, 3],
    [4, 5, 6]]
print(t[0][2])