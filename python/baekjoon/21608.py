"""
https://www.acmicpc.net/problem/21608
상어 초등학교 - [G5]21608

구현
"""

from sys import stdin

def solution(N, A):
    C = [[0]*N for _ in range(N)]

    for i in range(N**2):
        target, f1,f2,f3,f4 = A[i]

        # 1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.


    # 2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.

    # 3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.

    # 학생들의 만족도 계산
    answer = 0

    return answer

# input
N = int(stdin.readline())
A = [list(map(int,stdin.readline().rstrip().split())) for _ in range(N**2)]

# response
response = solution(N, A)
print(response)