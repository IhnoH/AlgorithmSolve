s = 'ApPApPpAPpApPApPAp'
ppap = 'pPAp'
cnt = 0
i = 0
while i < len(s)-3:
    if ppap == s[i:i+4]:
        cnt += 1
        print(s[i:i+4])
        i += 3
    i += 1

print(len(s), cnt)
