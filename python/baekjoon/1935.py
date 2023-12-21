"""
https://www.acmicpc.net/problem/1935
후위 표기식2 - [S3]1935

Data Structures, Stack
"""

# 1 ≤ N ≤ 26

from sys import stdin
from string import ascii_uppercase

def solution(N, string, value_array):
    answer = 0 
    array = list(string)
    # 알파벳을 대응하는 값으로 변환
    A_array = list(ascii_uppercase)
    for index,value in enumerate(array):
        if value in A_array:
            a_index = A_array.index(value)
            array[index] = value_array[a_index]
    # 연산 수행 - 스택 구조 활용
    stack = []
    for value in array:
        if value in ['+', '-', '*', '/']:
            v1 = stack.pop()
            v2 = stack.pop()
            tmp = eval(''.join([str(v2),value,str(v1)]))
            stack.append(tmp)
        else:
            stack.append(value)
    answer = tmp
    # print answer
    print(format(answer,'.2f'))

# input
N = int(stdin.readline().rstrip())
string = stdin.readline().rstrip()
value_array = [int(stdin.readline().rstrip()) for _ in range(N)]

solution(N, string, value_array)

# 후위 표기식: 연산자가 피연산자들보다 뒤에 나오는 식, 연산자는 왼쪽부터 사용하고 피연산자는 오른쪽부터 사용됨.
# from string import ascii_lowercase, ascii_uppercase로 알파벳을 불러와서 사용 가능
# python에서 stack은 그냥 기본 리스트 자료구조의 append(), pop()을 활용하여 구현 가능
# python 내장 함수 eval()을 통해 문자열로 되어있는 수식 계산 가능
# str.join()은 하나의 인풋값(리스트)를 받아 하나의 연결된 문자열로 반환
# format() 함수를 통해 출력값 소수점 설정