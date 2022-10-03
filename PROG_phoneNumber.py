def solution(phone_number):

    return len(phone_number[:-4])*'*'+phone_number[-4:]

print(solution("01033334444"))

print('01033334444'[:-4])
