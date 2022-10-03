from collections import deque

case = int(input())
for _ in range(case):
    n = int(input())
    conn = list(map(int, input().split(' ')))
    graph = {i:[] for i in range(1, n+1)}
    for i in range(1, n+1):
        graph[i].append(conn[i-1])

    queue = deque([1])

    visited = [False]*(n+1)

    visited[1] = visited[0] = True

    tmp = []
    answer = []
    while queue:
        node = queue.popleft()
        tmp.append(node)
        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
            else:
                answer.append(tmp)
                tmp = []
                if False in visited:
                    queue.append(visited.index(False))
    print(len(answer))
