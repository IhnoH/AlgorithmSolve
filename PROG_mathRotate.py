def solution(answers):
    answer = []

    fst = 0
    sec = 0
    thr = 0


    secAns = [1, 3, 4, 5]
    thrAns = [3, 1, 2, 4, 5]

    for i, n in enumerate(answers):


        if n == (i+1) % 6:
            fst += 1

        if 0 == (i % 2) and n == 2:
            print(2)
            sec += 1
        elif i % 2 and n == secAns[int(i/2)]:
            print(secAns[int(i/2)])
            sec += 1

        if n == thrAns[int(i / 2)]:
            thr += 1


    print(fst, sec, thr)

    return answer


solution([1,3,2,4,2])


