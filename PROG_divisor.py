def solution(left, right):
    answer = 0

    for n in range(left, right+1):
        t = len([i for i in range(1, n+1) if not n % i])
        if t%2: answer -= n
        else: answer += n

    return answer

print(solution(24, 27))