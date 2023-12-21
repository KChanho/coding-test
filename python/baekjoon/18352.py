"""
https://www.acmicpc.net/problem/18352
특정 거리의 도시 찾기 - [S2]

Graph Theory, Graph Traversal, Breadth-first Search, Dijkstra's
"""

# 2 ≤ N ≤ 300,000, 1 ≤ M ≤ 1,000,000, 1 ≤ K ≤ 300,000, 1 ≤ X ≤ N

from sys import stdin
from collections import deque

def solution(N, K, X, graph):
    # X에서 출발했을 때, 최단거리 계산 => bfs
    distance = [-1]*(N+1)
    distance[X] = 0
    # BFS
    q = deque([X])
    while q:
        now = q.popleft()
        for nxt in graph[now]:
            if distance[nxt] == -1:
                distance[nxt] = distance[now]+1
                q.append(nxt)

    # K값이 distance에 있다면 i값출력 없다면 -1 출력
    if K in distance:
        for i in range(1, N+1):
            if distance[i] == K:
                print(i)
    else:
        print(-1)

# input
N, M, K, X = map(int, stdin.readline().rstrip().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int, stdin.readline().rstrip().split())
    graph[a].append(b)

solution(N, K, X, graph)

# * 연산자는 shallow copy를 수행하므로, 2차원 배열의 선언은 * 연산자가 아닌 반복문을 통해서 수행해야 함.
# 메모리 초과... 계속 넣다보니 queue가 너무 커지는게 아닐까? -> bfs에서 다음 타겟을 넣는 부분을 더 깔끔히 정리하자