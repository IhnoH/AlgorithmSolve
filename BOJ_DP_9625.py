k = 46#int(input())


def BABBA(n):
    dp[1] = 1
    if n == 1: return 0, 1
    for i in range(2, n+1):
        dp[i] = dp[i-2]+dp[i-1]
    return dp[n-1], dp[n]

for i in range(1, 46):
    dp = [0] * (i + 1)
    a, b= BABBA(i)
    print(i, a, b)

