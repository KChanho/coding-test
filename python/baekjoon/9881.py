"""
https://www.acmicpc.net/problem/9881
Ski Course Design - [S5]9881

Bruteforcing, Sweeping
"""

# 1 <= N <= 1,000
# 0 <= integer elevation <= 100

# N과 높이의 범위가 작으므로, 가능한 모든 경우에 대해 계산 가능

from sys import stdin
import math

def calc_cost(min, max, array):
    cost = 0
    for h in array:
        if h < min:
            cost += (min - h)**2
        elif h > max:
            cost += (h - max)**2
    return cost

def solution(N, array):
    answer = math.inf
    flag = 0
    m, n = max(array), min(array)
    for i in range(n, m-17 + 1):
        tmp = calc_cost(i, i+17, array)
        if tmp > 0:
            flag = 1
            answer = min(answer, tmp)
    if flag == 0:
        answer = 0
    print(answer)

N = int(stdin.readline().rstrip())
array = [int(stdin.readline().rstrip()) for _ in range(N)]

solution(N, array)