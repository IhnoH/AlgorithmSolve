import itertools

def solution(nums):
    answer = 0
    prime = list(map(lambda x: sum(x), list(itertools.combinations(nums, 3))))

    for p in prime:
        if not len([i for i in range(2, p) if p%i == 0]):
            answer+=1

    return answer


print(solution([1,2,7,6,4]))

