"""
https://www.acmicpc.net/problem/15059
Hard choice - [B4]15059

Mathematics, Implementation, Arithmetic
"""

# (0 ≤ Ca, Ba, Pa ≤ 100), (0 ≤ Cr, Br, Pr ≤ 100)

from sys import stdin

def solution(A, R):
    answer = 0
    for a,r in zip(A, R):
        if r > a:
            answer += r-a
    print(answer)

A = list(map(int, stdin.readline().rstrip().split()))
R = list(map(int, stdin.readline().rstrip().split()))

solution(A, R)