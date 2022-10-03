# https://school.programmers.co.kr/learn/courses/30/lessons/67256
def solution(numbers, hand):
    answer = ''
    keypad = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9],
              [-1, 0, -2]]

    right = [3, 2]
    left = [3, 0]

    for n in numbers:
        cur = [[keypad.index(i), i.index(n)] for i in keypad if n in i][-1]

        if cur[1] == 0:
            answer = answer + 'L'
            left = cur
            continue
        elif cur[1] == 2:
            answer = answer + 'R'
            right = cur
            continue

        r = abs(right[0] - cur[0]) + abs(right[1] - cur[1])
        l = abs(left[0] - cur[0]) + abs(left[1] - cur[1])

        if r < l or (r == l and hand == 'right'):
            answer = answer + 'R'
            right = cur
        else:
            answer = answer + 'L'
            left = cur

    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))

keypad2 = {1: [0, 0], 2: [0, 1], 3: [0, 2],
           4: [1, 0], 5: [1, 1], 6: [1, 2],
           7: [2, 0], 8: [2, 1], 9: [2, 2],
           -1: [3, 0], 0: [3, 1], -2: [3, 2]}
