"""
https://www.acmicpc.net/problem/13627
Dangerous Dive - [B2]13627

Implementation
"""

from sys import stdin

def solution(N, R, rlist):
    flag = 0
    for i in range(1, N+1):
        if i in rlist:
            continue
        else:
            print(i, end=' ')
            flag = 1
    if flag == 0:
        print('*')

N, R = map(int, stdin.readline().rstrip().split())
rlist = list(map(int, stdin.readline().rstrip().split()))

solution(N, R, rlist)