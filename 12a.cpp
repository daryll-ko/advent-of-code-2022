#include "bits/stdc++.h"

using namespace std;

const int N = 41;
const int M = 172;

const int DI[4] = { 0, -1, 0, 1 };
const int DJ[4] = { 1, 0, -1, 0 };

int main() {
	int map[N][M], si, sj, ti, tj;
	for (int i = 0; i < N; ++i) {
		string row;
		cin >> row;
		for (int j = 0; j < M; ++j) {
			if (row[j] == 'S') {
				map[i][j] = 0;
				si = i, sj = j;
			} else if (row[j] == 'E') {
				map[i][j] = 25;
				ti = i, tj = j;
			} else {
				map[i][j] = row[j] - 'a';
			}
		}
	}
	int distance[N][M];
	bool visited[N][M];
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < M; ++j) {
			distance[i][j] = 123'456'789;
			visited[i][j] = false;
		}
	}
	queue<pair<int, int>> q;
	distance[si][sj] = 0;
	q.emplace(si, sj);
	while (!q.empty()) {
		auto [i, j] = q.front();
		q.pop();
		for (int d = 0; d < 4; ++d) {
			int i_to = i + DI[d], j_to = j + DJ[d];
			if (!(0 <= i_to && i_to < N && 0 <= j_to && j_to < M)) {
				continue;
			}
			if (map[i_to][j_to] - map[i][j] <= 1 && distance[i_to][j_to] > distance[i][j] + 1) {
				distance[i_to][j_to] = distance[i][j] + 1;
				q.emplace(i_to, j_to);
			}
		}
	}
	cout << distance[ti][tj] << '\n';
}