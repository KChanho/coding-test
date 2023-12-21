"""
https://www.acmicpc.net/problem/6373
Round and Round We Go - [S3]6373

Mathematics, Implementation, String, Arithmetic, Simulation, Arbitrary Precision / Big Integers
"""

from sys import stdin

def solution(integer):
    n = len(integer)
    for i in range(1, n+1):
        flag = 0
        tmp = str(int(integer) * i)
        # 자릿수가 부족한 경우 앞에 0을 채우기
        if len(tmp) < n:
            tmp = '0'*(n-len(tmp)) + tmp
        for j in range(n):
            if integer == tmp[j:] + tmp[:j]:
                flag = 1
                break
        if flag == 0:
            print(integer, "is not cyclic")
            return
    # print answer
    print(integer, "is cyclic")

# input
for line in stdin:
    integer = line.rstrip()
    solution(integer)

# f-strings: print("{변수} 문자열")
# 입력 줄수가 정해지지 않았을 때, sys.stdin 사용