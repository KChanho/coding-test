"""
https://www.acmicpc.net/problem/18429
근손실 - [S3]18429

Bruteforcing, Backtracking
"""

# 1 ≤ N ≤ 8 | 1 ≤ K ≤ 50 | 1 ≤ A ≤ 50
# N이 작으므로 가능한 모든 경우를 탐색

from sys import stdin

def solution(N, K, array):
    answer = 0
    visited = [0]*N
    # backtracking
    def backtracking(k, weight):
        nonlocal answer
        # 가지치기
        if weight < 0:
            return
        if k >= N:
            answer += 1
            return
        # 경우의 수 탐색
        for i in range(N):
            if visited[i] == 0:
                visited[i] = 1
                backtracking(k+1, weight+array[i]-K)
                visited[i] = 0
    backtracking(0, 0)
    # print answer
    print(answer)

# input
N, K = map(int, stdin.readline().rstrip().split())
array = list(map(int, stdin.readline().rstrip().split()))

solution(N, K, array)

# 백트래킹 알고리즘 활용 - 경우의 수를 탐색하다가, 가망이 없는 경우의 수는 가지치기
# 이미 사용한 경우의 수를 표시하기 위해 visited 리스트 필요
# global: 일반 함수 내에서 전역(global/module) 변수를 대상으로 사용, nonlocal: 중첩 함수 내에서 비지역(nonlocal/closing) 변수를 대상으로 사용