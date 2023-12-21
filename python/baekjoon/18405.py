"""
https://www.acmicpc.net/problem/18405
경쟁적 전염 - [G5]

Implementation, Graph Theory, Graph Traversal, Breadth-first Search
"""

# 1 ≤ N ≤ 200, 1 ≤ K ≤ 1,000

import sys; input = sys.stdin.readline
from collections import deque

d = [[1,0],[0,1],[-1,0],[0,-1]]

def bfs():
    virus = []
    for r in range(N):
        for c in range(N):
            if graph[r][c] != 0:
                virus.append((graph[r][c], 0, r, c))
    virus.sort()    # 바이러스를 k의 오름차순으로 정렬
    q = deque(virus) 
    while q:
        k,t,r,c = q.popleft()
        if t == S:
            break
        for dy,dx in d:
            if 0<=r+dy<N and 0<=c+dx<N and graph[r+dy][c+dx] == 0:
                graph[r+dy][c+dx] = k
                q.append((k,t+1,r+dy,c+dx))

if __name__ == "__main__":
    # input
    N, K = map(int, input().rstrip().split())
    graph = [list(map(int, input().rstrip().split())) for _ in range(N)]
    S, X, Y = map(int, input().rstrip().split())
    # solution
    bfs()
    # print
    print(graph[X-1][Y-1])

# 너무 많은 for 문의 반복으로 인해 시간초과... => 반복문 대신, bfs를 활용(전파 횟수 제한)