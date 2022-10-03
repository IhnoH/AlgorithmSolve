# https://school.programmers.co.kr/learn/courses/30/lessons/12906
def solution(arr):
    answer = []
    for i in arr:
        if len(answer) != 0:
            if answer[-1] == i:
                continue
        answer.append(i)
    return answer

print(solution( [4, 4, 4, 3, 3] ))