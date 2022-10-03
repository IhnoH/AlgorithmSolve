num = 100#int(input())
dp = [0]*(num+1)

def fibo_recur(n):
    if dp[n] != 0: return dp[n]
    if n == 1 or n == 0:
        dp[n] = n
        return n
    dp[n] = fibo_recur(n-1) + fibo_recur(n-2)
    return dp[n]

#print(fibo_recur(num))

print(fibo_recur(5))
print(dp[5]/dp[3])
