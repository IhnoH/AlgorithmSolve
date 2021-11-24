k = 3#int(input())
dp = [0] * (k + 1)

def tile(n):
    dp[1] = 1
    if n == 1: return 1
    for i in range(2, n+1):
        dp[i] = dp[i-2]+dp[i-1]
tile(k)
res = (dp[k]*2)+(dp[k-1]+dp[k])*2
print(res)