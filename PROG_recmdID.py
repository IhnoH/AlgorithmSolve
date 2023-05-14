def solution(new_id):
    answer = ''

    for c in new_id:
        # print(c, ord(c), answer)
        if 65 <= ord(c) <= 90:  # 대문자
            answer += chr(ord(c) + 32)
        elif (97 <= ord(c) <= 122) or (48 <= ord(c) <= 57) or (ord(c) == 95) or (
                45 <= ord(c) <= 46) or ord('.') == c:  # 소문자, 숫자, 빼기, 밑줄, 마침표
            answer += c

    while '..' in answer: answer = answer.replace('..', '.')

    print(answer)

    answer = answer.strip('.')
    if len(answer) > 15: answer = answer[:15]
    answer = answer.strip('.')
    if len(answer) == 0: answer = 'a'
    while len(answer) < 3: answer += answer[-1]

    return answer

tc = ["...!@BaT#*..y.abcdefghijklm"	,
        "z-+.^.",
        "=.=",
        "123_.def",
        "abcdefghijklmn.p"
]

print(solution('...!@BaT#*..y.abcdefghijklm'))
# for i in tc:
#     print(solution(i))
