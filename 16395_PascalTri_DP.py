num, K = (input()).split(' ')
num = int(num)
K = int(K)
dp = [[0]*(num+1) for _ in range(num+1)]

def binomial(n, k):
    if k == 1 or k == n: return 1
    for i in range(n):
        for j in range(min(i, k)+1):
            if j == 0 or j == i: dp[i][j] = 1
            else: dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    return dp[n-1][k-1]

print(binomial(num, K))
