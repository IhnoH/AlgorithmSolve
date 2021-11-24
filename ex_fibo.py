import sys

def memoization_fibo(n):
    memo[0] = 1
    memo[1] = 1

    if n<2: return memo[n]
    for i in range(2, n+1):
        memo[i] = memo[i-2] + memo[i-1]
    return memo[n]

def bottomUp_fibo(n):
    if n <= 1: return n
    fir = 0
    sec = 1
    for i in range(0, n-1):
        next = fir+sec
        fir = sec
        sec = next
    return next

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    memo = [0 for i in range(n+2)]
    print('memo:', memoization_fibo(n))
    print('bottom up:', bottomUp_fibo(n))