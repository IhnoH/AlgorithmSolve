# https://www.acmicpc.net/problem/9466
from collections import deque
from sys import stdin

def dfs(node):
    visited = []
    needVisit = deque([node])

    while needVisit:
        #print(needVisit)
        node = needVisit.pop()

        if not visit[node]:
            visited.append(node)
            visit[node] = 1
            needVisit.append(g[node])
            if g[node] in visited:
                #print(node, visited, needVisit)
                tmp = visited[:visited.index(g[node])]
                noTeam.extend(tmp)
                for j in visited: visit[j] = 2
                return

        if visit[node] == 2 or g[node] == g[g[node]]:
            noTeam.extend(visited)
            visited.append(g[node])
            for j in visited: visit[j] = 2
            return



tc = int(stdin.readline())

for _ in range(tc):
    n = int(stdin.readline())
    g = [0]
    g.extend(list(map(int, stdin.readline().split(' '))))
    noTeam = []
    visit = [0] * (n + 1)
    visit[0] = 1
    #print(g)
    while 0 in visit:
        node = visit.index(0)
        dfs(node)
    #print(noTeam)
    print(len(noTeam))

""" test
7
6
2 3 4 5 6 2
5
2 5 4 5 2
6
1 3 4 3 2 6
13
2 4 5 2 4 1 8 9 10 11 9 10 10
10
2 5 7 1 6 8 8 3 5 10
10
2 7 10 5 3 3 9 10 6 3
6
2 1 1 2 6 3

import sys
sys.setrecursionlimit(111111) #충분한 재귀 깊이를 주어 오류를 예방


def dfs(x):
    global result
    visited[x] = True
    cycle.append(x) #사이클을 이루는 팀을 확인하기 위함
    number = numbers[x]
    
    if visited[number]: #방문가능한 곳이 끝났는지
        if number in cycle: #사이클 가능 여부
            result += cycle[cycle.index(number):] #사이클 되는 구간 부터만 팀을 이룸
        return
    else:
        dfs(number)


for _ in range(int(input())):
    N = int(input())
    numbers = [0] + list(map(int, input().split()))
    visited = [True] + [False] * N #방문 여부
    result = []
    
    for i in range(1, N+1):
        if not visited[i]: #방문 안한 곳이라면
            cycle = []
            dfs(i) #DFS 함수 돌림
            
    print(N - len(result)) #팀에 없는 사람 수
"""