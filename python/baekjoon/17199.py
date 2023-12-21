"""
https://www.acmicpc.net/problem/17199
Milk Factory - [S1]

Graph Theory, Graph Traversal, Depth-first Search
"""

# 1 <= N <= 100

from sys import stdin

def solution(N, graph):
    # The station which all others should be able to reach
	root = -1
	# Check all stations and see if they can be the root
	for s in range(N):
		visited = [False]*N
		# We can always reach a station from itself
		visited[s] = True

		# Our stack for DFS
		vector<int> todo{s};
		while (!todo.empty()) {
			int curr = todo.back();
			todo.pop_back();
			for (int n : neighbors[curr]) {
				// Make sure to only visited unvisited nodes
				if (!visited[n]) {
					visited[n] = true;
					todo.push_back(n);
				}
			}
		}

		// Check if all nodes have been visited
		bool valid = true;
		for (int check_s = 0; check_s < station_num; check_s++) {
			if (!visited[check_s]) {
				valid = false;
				break;
			}
		}

		if (valid) {
			root = s + 1;
			break;
		}
	}

	std::ofstream("factory.out") << root << endl;
    """

# input
N = int(stdin.readline().rstrip())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int, stdin.readline().rstrip().split())
    graph[a].append(b)

solution(N, graph)

# dfs를 재귀함수로 구현했을 때, 종료 조건과 결과값을 전달하는 방식에 익숙하지 않음
# dfs로도 풀이할 수 있지만, 규칙을 찾아서 풀이 가능