def solution(survey, choices):
    result = ''

    p = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'M': 0, 'J': 0, 'A': 0, 'N': 0}

    for s, c in zip(survey, choices):
        c -= 4
        if c < 0: p[s[0]] += abs(c)
        elif c > 0: p[s[1]] += abs(c)

    k = list(p.keys())
    for i in range(0, len(k), 2):
        if p[k[i]] == p[k[i+1]]:
            result += min(k[i], k[i+1])
        elif p[k[i]] > p[k[i+1]]:
            result += k[i]
        else:
            result += k[i+1]

    return result


print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
