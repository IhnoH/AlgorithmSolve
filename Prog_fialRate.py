def solution(N, stages):
    tmp = {}
    for n in range(1, N+1):
        success = len([s for s in stages if n <= s])
        if success == 0:
            tmp[n] = 0
            continue

        fail = len([s for s in stages if n == s])/success
        tmp[n] = fail

    d2 = sorted(tmp.items(), key=lambda x:x[1], reverse=True)

    return [i[0] for i in d2]



print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))

print(solution(4, [4,4,4,4,4]))

print(solution(5, [3, 3,3 ,3]))