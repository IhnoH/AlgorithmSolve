#https://www.acmicpc.net/problem/15958

import math
n = int(input())
xList, yList = [],[]
y_min = math.inf
x_max = -math.inf
x_ = 0
tmp = 0
tmp_ = 0
tp = 0
for i in range(n):
    x, y = input().split(' ')
    x = int(x)
    y = int(y)

    xList.append(x)
    yList.append(y)

    # 조건 없이 계속 차이를 구하다 큰값
    tmp = x-x_
    if tmp > x_max:
        x_max = tmp
    
    ''' # x 전후의 차이가 제일 큰값
    if x_ != x:
        if x - x_ > x_max:
            x_max = x-x_
        x_ = x
    #'''
    if y < y_min and y != 0: y_min = y


print(x_max)
y_max = max(yList)

'''
히스토그램이 계단식으로 되어있을때 x는 끊겨있고 길이가 길어
조건을 충족하지만 끊겨있는 x위로 y가 여유가 있을 때 조건이 고민

testcase
12
0 0
0 6
2 6
2 3
4 3
4 7
12 7
12 5
13 5
13 8
15 8
15 0
'''