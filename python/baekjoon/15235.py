"""
https://www.acmicpc.net/problem/15235
Olympiad Pizza - [S5]15235

Implementation, Data Structures, Simulation, Queue
"""

# N <= 1,000    1 <= numbers in the sequence <= 1000    1 <= Each contestant will need <= 100

from sys import stdin
from collections import deque

def solution(N, array):
    queue = deque(enumerate(array))
    answer = [0]*N
    count = 0
    while queue:
        index, left = queue.popleft()
        count += 1
        answer[index] = count
        left -= 1
        if left == 0:
            continue
        else:
            queue.append((index, left))
    # print answer
    print(' '.join(str(answer[i]) for i in range(N)))

# input
N = int(stdin.readline().rstrip())
array = list(map(int, stdin.readline().rstrip().split()))

solution(N, array)

# python의 효율적인 queue 자료구조: from collections import deque
# enumerate를 활용해서 index와 value를 함께 활용 가능