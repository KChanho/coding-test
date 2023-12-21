"""
https://www.acmicpc.net/problem/17086
아기 상어 2 - [S2]

Graph Theory, Bruteforcing, Graph Traversal, Breadth-first Search
"""

# 2 ≤ N, M ≤ 50

from sys import stdin
from collections import deque

def solution(N, M, graph):
    queue = deque()
    for i in range(N):
        for j in range(M):
            if graph[i][j] == '1':
                queue.append((i,j))
                graph[i][j] = 0

    def bfs():
        while queue:
            r,c = queue.popleft()
            for dy,dx in [(1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1)]:
                nr,nc = r+dy,c+dx
                if (nr >= 0 and nr < N) and (nc >= 0 and nc < M) and graph[nr][nc] == '0':
                    graph[nr][nc] = graph[r][c]+1
                    queue.append((nr,nc))

    bfs()
    answer = max(sum(graph,[]))

    # print answer
    print(answer)

# input
N, M = map(int, stdin.readline().rstrip().split())
graph = [stdin.readline().rstrip().split() for _ in range(N)]

solution(N, M, graph)

# sum(iterable, start): start에 iterable의 모든 데이터를 더하는 함수, 활용해서 2차원 list를 1차원으로 변환 가능.