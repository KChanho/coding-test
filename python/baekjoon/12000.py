"""
https://www.acmicpc.net/problem/12000
Circular Barn - [S4]12000

Bruteforcing
"""

# 3 <= n <= 1,000   1 <= ri <= 100

from sys import stdin
import math

def solution(n, r_array):
    answer = math.inf
    # 모든 경우에 대해 total amount of distance를 계산하여 비교
    for i in range(n):
        tmp = 0
        for j in range(n):
            tmp += r_array[j] * (j-i if j >= i else n+j-i)
        answer = min(answer, tmp)
    # print answer
    print(answer)

# input
n = int(stdin.readline().rstrip())
r_array = [int(stdin.readline().rstrip()) for _ in range(n)]

solution(n, r_array)

# one-line if문: <결과> if <조건> else <결과>