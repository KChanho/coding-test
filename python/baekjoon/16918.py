"""
https://www.acmicpc.net/problem/16918
봄버맨 - [S1]16918

Implementation, Graph Theory, Graph Traversal, Simulation
"""

# 1 ≤ R, C, N ≤ 200

from sys import stdin

def solution(R, C, N, graph):
    if N == 1:  # 초기상태
        for i in range(R):
            print(''.join(graph[i]))
        return
    elif N % 2 == 0:    # N이 짝수일 때, graph는 전부다 O
        for i in range(R):
            print('O'*C)
        return
    else:
        tmp1 = [['O'] * C for _ in range(R)]    # 한 번 폭발
        for i in range(R):
            for j in range(C):
                if graph[i][j] == 'O':  # 폭탄이 있는 자리면, 폭발
                    tmp1[i][j] = '.'
                else:   # 폭탄이 있는 자리가 아니라면, 근처에 폭탄이 있는지 확인
                    for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
                        if (i+x >= 0 and i+x < R) and (j+y >= 0 and j+y < C) and graph[i+x][j+y] == 'O':
                            tmp1[i][j] = '.'
                            break
        tmp2 = [['O'] * C for _ in range(R)]    # 두 번 폭발
        for i in range(R):
            for j in range(C):
                if tmp1[i][j] == 'O':  # 폭탄이 있는 자리면, 폭발
                    tmp2[i][j] = '.'
                else:   # 폭탄이 있는 자리가 아니라면, 근처에 폭탄이 있는지 확인
                    for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
                        if (i+x >= 0 and i+x < R) and (j+y >= 0 and j+y < C) and tmp1[i+x][j+y] == 'O':
                            tmp2[i][j] = '.'
                            break
        if N % 4 == 3:
            for i in range(R):
                print(''.join(tmp1[i]))
            return
        else:
            for i in range(R):
                print(''.join(tmp2[i]))
            return

R, C, N = map(int, stdin.readline().rstrip().split())
graph = [list(stdin.readline().rstrip()) for _ in range(R)]

solution(R, C, N, graph)

# 예제 기반 규칙성 찾아보기 -> N % 4 == 1일 때, 초기 상태와 다른 경우도 있을 수 있음
# 0과 O 구분...