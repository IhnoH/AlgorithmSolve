from collections import deque

def solution(board, moves):
    answer = 0
    print(*board, sep='\n', end='\n\n')
    dep = len(board)
    q = deque([-1])
    for i in moves:
        i -= 1
        for j in range(dep):
            if board[j][i] != 0:
                if board[j][i] == q[-1]:
                    q.pop()
                    answer += 2
                else:q.append(board[j][i])

                board[j][i] = 0
                break

    print(*board, sep='\n', end='\n')

    return answer


print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))


q = deque([-1])
q.append(1)
q.append(2)
q.pop()
print(q)