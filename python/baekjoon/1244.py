"""
https://www.acmicpc.net/problem/1244
스위치 켜고 끄기 - [S4]1244

Implementation, Simulation
"""

# 1 <= N <= 100 | 1 <= S <= 100

from sys import stdin

def solution(N, status_array, S, student_array):
    answer = status_array[:]
    for sex,number in student_array:
        if sex == 1:    # 남학생일 경우: 스위치 번호가 자기가 받은 수의 배수이면, 그 스위치의 상태를 바꿈
            for i in range(1,N+1):
                if i%number == 0:
                    answer[i-1] = 0 if answer[i-1] == 1 else 1
        elif sex == 2:   # 여학생일 경우: 스위치 번호를 중심으로 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서, 그 구간에 속한 스위치의 상태를 모두 바꿈
            answer[number-1] = 0 if answer[number-1] == 1 else 1
            for i in range(1, N//2+1):
                if number-1-i < 0 or number-1+i > N-1:
                    break
                elif answer[number-1-i] != answer[number-1+i]:
                    break
                else:
                    answer[number-1-i] = 0 if answer[number-1-i] == 1 else 1
                    answer[number-1+i] = 0 if answer[number-1+i] == 1 else 1
    # print answer
    for i in range(1, N + 1):
        print(answer[i-1], end=' ')
        if i % 20 == 0:
            print()

# input
N = int(stdin.readline().rstrip())
status_array = list(map(int, stdin.readline().rstrip().split()))
S = int(stdin.readline().rstrip())
student_array = [tuple(map(int, stdin.readline().rstrip().split())) for _ in range(S)]

solution(N, status_array, S, student_array)

# 일정 간격으로 줄바꿈하는 출력
# 1부터 시작하는 배열의 경우 인덱스와 혼동에 유의