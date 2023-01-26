# https://www.acmicpc.net/problem/7576
from sys import stdin
from collections import deque

import numpy as np

n, m = map(int, stdin.readline().split(' '))
g = []
for i in range(m):
    g.append(list(map(int, stdin.readline().split(' '))))

d = [(-1, 0), (0, -1), (0, 1), (1, 0)]

