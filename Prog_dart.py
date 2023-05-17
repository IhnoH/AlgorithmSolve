def solution(dartResult):
    answer = 0
    tmp = 0
    l = [0]
    for i in dartResult:
        if ord('0') <= ord(i) <= ord('9'):
            if '0' == i and tmp == 1: tmp *= 10
            else:
                l.append(tmp)
                tmp = int(i)

        if 'D' == i: tmp = tmp**2
        elif 'T' == i: tmp = tmp**3
        elif '#' == i: tmp *= (-1)
        elif '*' == i:
            tmp *= 2
            l[-1] *= 2

    l.append(tmp)
    return sum(l)

a = ['1S2D*3T','1D2S#10S','1D2S0T','1S*2T*3S','1D#2S*3S','1T2D3D#','1D2S3T*']

for j in a:
    print(j, solution(j))
    print()
