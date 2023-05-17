def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        a = bin(arr1[i] | arr2[i])[2:].zfill(n)
        b = a.replace("1", "#").replace("0", " ")
        answer.append(b)
    return answer

print(solution(5, [0,0, 0, 0, 0],[30, 1, 21, 17, 28]))
