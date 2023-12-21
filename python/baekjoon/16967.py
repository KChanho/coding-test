"""
https://www.acmicpc.net/problem/16967
배열 복원하기 - [S3]16967

Implementation
"""

# 2 ≤ H, W ≤ 300    1 ≤ X < H   1 ≤ Y < W   0 ≤ Bi,j ≤ 1,000

from sys import stdin

def solution(H, W, X, Y, B):
    A = [[0]*W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            # 겹치지 않는 부분: 앞뒤에서 각각 X,Y개의 행,열
            if i <= X-1 or j <= Y-1:    # 0~X-1, 0~Y-1
                A[i][j] = B[i][j]
            elif i >= H-X or j >= W-Y:  # W-X~W-1, H-Y~H-1
                A[i][j] = B[i+X][j+Y]
            # 겹친 부분을 통해서만 구할 수 있는 부분
            else:   # Bi,j = Ai,j + Ai-X,j-Y인데, 위에서부터 A를 구하므로 Ai-X,j-Y는 이미 알고 있는 상태
                A[i][j] = B[i][j] - A[i-X][j-Y]
    
    # print answer
    for i in range(H):
        # 리스트를 한 줄의 문자열로 변환하여 출력
        print(' '.join(str(A[i][j]) for j in range(W)))
    
H, W, X, Y = map(int, stdin.readline().rstrip().split())
B = [list(map(int, stdin.readline().rstrip().split())) for _ in range(H+X)]

solution(H, W, X, Y, B)

# 주어진 조건에 따라 구현하기 - 예제를 활용하여 규칙 찾기!
# 인덱스 범위 확인하기(등호도 체크!)
# 출력 형태 확인하기
# 행, 열 헷갈리지 말기!