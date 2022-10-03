def solution(id_list, report, k):
    report = list(set(report))
    reporting = [i.split(' ')[0] for i in report]
    reported = [i.split(' ')[1] for i in report]
    n = [i for i in id_list if reported.count(i) >= k]
    mail = [reporting[i] for i in range(len(reporting)) if reported[i] in n]
    answer = [mail.count(i) for i in id_list]

    return answer


print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))

