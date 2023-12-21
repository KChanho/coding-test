"""
https://www.acmicpc.net/problem/16234
인구이동 - [G5]16234

2차원 배열 상에서 인접한 칸 사이의 관계를 확인하는 문제이므로 BFS를 사용
"""

import sys
input = sys.stdin.readline

import math
from collections import deque

N, L, R = map(int, input().rstrip().split())
A = [list(map(int, input().rstrip().split())) for _ in range(N)]

# direction
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(r, c):
    """
    dq: deque for BFS
    visited: 방문 여부 리스트
    union: 연합 국가 리스트
    count: 연합 국가 인구 총합
    """
    dq = deque()
    dq.append((r, c))
    visited[r][c] = True
    union = [(r, c)]
    count = A[r][c]
    while dq:
        x, y = dq.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if visited[nx][ny]:
                continue
            if L <= abs(A[nx][ny] - A[x][y]) <= R:
                union.append((nx, ny))
                visited[nx][ny] = True
                dq.append((nx, ny))
                count += A[nx][ny]
    for x, y in union:
        A[x][y] = math.floor(count / len(union))
    return len(union)

result = 0    
while True:
    """
    flag: 인구 이동 여부 플래그
    """
    visited = [[False] * N for _ in range(N)]
    flag = False
    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                if bfs(r, c) > 1:
                    flag = True
    if not flag:
        break
    result += 1

print(result)