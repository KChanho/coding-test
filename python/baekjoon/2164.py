"""
https://www.acmicpc.net/problem/2164
카드 2 - [S4]2164

Data Structures, Queue
"""

# 1 ≤ N ≤ 500,000

from sys import stdin
from collections import deque

def solution(N):
    queue = deque(list(range(1, N+1)))
    while len(queue) > 1:
        queue.popleft()
        tmp = queue.popleft()
        queue.append(tmp)
    # print answer
    answer = queue.popleft()
    print(answer)

# input
N = int(stdin.readline().rstrip())

solution(N)

# deque 시간복잡도: popleft() - O(1), append() - O(1)