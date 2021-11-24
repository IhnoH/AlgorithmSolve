import time
t = time.time()
num = 10#int(input())
dp = [0]*(num+1)

def sumCombinate_recur(n):
    if dp[n] != 0: return dp[n]
    if n == 1 or n == 2:
        dp[n] = n
        return n
    elif n==3:
        dp[n] = n+1
        return dp[n]
    dp[n] = sumCombinate_recur(n-1) + sumCombinate_recur(n-2) + sumCombinate_recur(n-3)
    return dp[n]

print(sumCombinate_recur(num), time.time()-t)

'''
1: 1
2: 2
3: 4
4: 7
5: 12

'''