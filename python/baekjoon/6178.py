"""
https://www.acmicpc.net/problem/6178
Lake Making - [S4]6178

Implementation, Simulation
"""

# 3 <= R <= 100 | 3 <= C <= 100 | 10 <= elev_rc <= 5000
# 1 <= R_s <= R-2 | 1 <= C_s <= C-2 | 1 <= D_s <= 40
# 1 <= N <= 20000 | 0 <= E <= 5000

from sys import stdin

def solution(R, C, E, N, map_array, instruction_array):
    # instruction
    for Rs,Cs,Ds in instruction_array:
        m = max(max(map_array[Rs-1][Cs-1:Cs-1+3]), max(map_array[Rs][Cs-1:Cs-1+3]), max(map_array[Rs+1][Cs-1:Cs-1+3]))
        for i in range(3):
            for j in range(3):
                if map_array[Rs-1+i][Cs-1+j] > m-Ds: map_array[Rs-1+i][Cs-1+j] = m-Ds
    # calculate volume of the new lake in cubic inches
    total = 0
    for i in range(R):
        for j in range(C):
            if map_array[i][j] < E: total += E - map_array[i][j]
    # print answer
    print(total*72*72)

# input
R, C, E, N = map(int, stdin.readline().rstrip().split())
map_array = [list(map(int, stdin.readline().rstrip().split())) for _ in range(R)]
instruction_array = [tuple(map(int, stdin.readline().rstrip().split())) for _ in range(N)]

solution(R, C, E, N, map_array, instruction_array)

# 지문이 장문의 영문이라 시간이 다소 소요됨
# 행, 열 헷갈리지 말기!