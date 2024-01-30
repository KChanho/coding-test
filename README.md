# [coding-test 문제풀이 유형별 정리](https://github.com/KChanho/coding-test)

이 페이지는 코딩 테스트 문제의 문제풀이를 유형별로 정리해놓은 페이지입니다.

- [그리디](https://github.com/KChanho/coding-test/Greedy)
- [구현](https://github.com/KChanho/coding-test/Implementation)
- [DFS/BFS](https://github.com/KChanho/coding-test/DFS-BFS)
- [정렬](https://github.com/KChanho/coding-test/Sorting)
- [이진 탐색](https://github.com/KChanho/coding-test/Binary-Search)
- [다이나믹 프로그래밍](https://github.com/KChanho/coding-test/Dynamic-Programming)
- [최단 경로](https://github.com/KChanho/coding-test/Shortest-Path)
- [그래프 이론](https://github.com/KChanho/coding-test/Graph-Theory)

> 코딩테스트 문제의 유형별 분류는 나동빈 님의 `이것이 취업을 위한 코딩 테스트다`를 참고했습니다.



## 문제풀이 파일명 정보
문제풀이 파일명에 코딩 테스트 문제의 출처(문제풀이 사이트)와 언어에 대한 정보를 담고 있습니다.

> `bj-10655.py`

위의 예시에서
- 접두사인 `bj`는 문제풀이 사이트인 `백준`을 의미하고
- `-` 이후에 이어지는 번호인 `10655`는 문제의 번호를 뜻하며
- 파일의 확장자인 `py`를 통해 python 언어로 작성된 문제풀이 파일임을 확인할 수 있습니다.

### 사이트 목록
- [Baekjoon Online Judge `bj`](https://www.acmicpc.net/)
- [Programmers `p`](https://programmers.co.kr/)

### 언어 목록
- Python `.py`
- SQL `.sql`

## 코딩테스트 문제풀이 TIP - 복잡도
복잡도는 알고리즘의 성능을 나타내는 척도로 많은 코딩 테스트에서 복잡도에 제한을 두고 있습니다. 따라서 코딩 테스트를 준비할 때, 복잡도를 고려하여 문제를 해결해야 합니다.

### 시간 복잡도
코딩 테스트의 제한 사항 중 `시간 제한`에 해당하는 부분으로 주어진 시간 안에 동작하는 프로그램을 작성해야 합니다.

일반적으로 시간 복잡도를 표현할 때는 `Big-O` 표기법을 사용하는데, 간단히 정리하면 가장 빠르게 증가하는 항만을 고려하는 표기법 입니다.

아래는 자주 등장하는 시간 복잡도 표 입니다.

| `Big-O` 표기법 | 명칭 |
| ----- | ----- |
| O(1) | 상수 시간 |
| O(logN) | 로그 시간 |
| O(N) | 선형 시간 |
| O(NlogN) | 로그 선형 시간 |
| O(N^2) | 이차 시간 |
| O(N^3) | 3차 시간 |
| O(2^n) | 지수 시간 |

이러한 표기법을 활용해 프로그램의 연산 횟수를 셈하여 시간 제한 내에서 작동하는 프로그램을 구현해야 합니다. 또, 동일한 시간제한이라도 프로그래밍 언어별 연산 처리 속도가 다르므로 허용가능한 연산 횟수가 다를 수 있습니다.

### 공간 복잡도
공간 복잡도는 코딩 테스트의 제한 사항 중 `메모리 제한`에 해당하는 부분으로 시간 복잡도와 마찬가지로 `Big-O` 표기법을 사용하여 계산합니다.

언어별, 자료형별 사용하는 메모리 크기가 다르므로 이를 고려하여 프로그램을 구성해야 합니다.

> 일반적으로 알고리즘에서 복잡도에 크게 영향을 주는 부분은 반복문 입니다. 특히 이중, 삼중 반복문을 수행할 때는 주의해야 합니다.

### 수행 시간 측정
python의 경우 아래와 같은 코드를 통해 프로그램 수행 시간을 측정할 수 있습니다.

```python
import time
start_time = time.time() # 측정 시작

# 프로그램 소스 코드

end_time = time.time() # 측정 종료
print("time :", end_time - start_time) # 수행 시간 출력
```