from functools import reduce


def solution(lottos, win_nums):
    answer = []
    low = list(filter(lambda n: n in win_nums, lottos))
    answer.append(7-len(low))
    zeroN = len(list(filter(lambda n:n == 0, lottos)))
    answer.insert(0, answer[0]-zeroN)
    if answer[0] > 6: answer[0] -= 1
    if answer[1] > 6: answer[1] -= 1
    return answer

print(solution([1,2,3,4,5,6], [7,8,9,10,11,12]))
print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0], [20, 9, 3, 45, 4, 35]))