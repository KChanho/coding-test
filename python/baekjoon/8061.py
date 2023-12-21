"""
https://www.acmicpc.net/problem/8061
Bitmap - [S2]8061

Graph Theory, Graph Traversal, Breadth-first Search
"""

# 1 ≤ n ≤ 182 | 1 ≤ m ≤ 182

from sys import stdin
from collections import deque

def solution(n, m, bitmap):
    # 흰색 픽셀의 위치를 큐에 추가
    queue = deque()
    for i in range(n):
        for j in range(m):
            if bitmap[i][j] == '1':
                bitmap[i][j] = 0
                queue.append((i,j))

    def bfs():  # bfs이므로 가장 가까운 거리부터 계산됨
        while queue:
            r,c = queue.popleft()
            for dy,dx in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr,nc = r+dy,c+dx
                if (nr >= 0 and nr < n) and (nc >= 0 and nc < m) and bitmap[nr][nc] == '0':
                    queue.append((nr,nc))
                    bitmap[nr][nc] = bitmap[r][c]+1

    bfs()

    # print answer
    for row in bitmap:
        print(*row)

# input
n, m = map(int, stdin.readline().rstrip().split())
bitmap = [list(stdin.readline().rstrip())for _ in range(n)]

solution(n, m, bitmap)

# bfs는 큐 자료구조를 활용
# list 앞에 *를 붙여주면 unpacking되는 효과를 가짐. sep 인자를 설정하여 구분자를 설정할 수도 있음.