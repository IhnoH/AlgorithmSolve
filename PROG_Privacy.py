# https://school.programmers.co.kr/learn/courses/30/lessons/150370
from sys import stdin

def solution(today, terms, privacies):
    trm = {}
    for i in terms:
        tmp = i.split(' ')
        trm[tmp[0]] = int(tmp[1])*28

    today = toDays(today)
    ans = []

    for id, pvc in enumerate(privacies):
        p = pvc.split(' ')
        if today >= toDays(p[0]) + trm[p[1]]:
            ans.append()
    return ans

def toDays(date):
    y, m, d = map(int, date.split('.'))
    return y*28*12 + m*28 + d


print(solution("20.01.01", ['Z 3', 'D 5'], ["19.01.01 D", "19.11.15 Z", "19.08.02 D", "19.07.01 D", '18.12.28 Z']))

