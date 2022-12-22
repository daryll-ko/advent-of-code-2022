#include "bits/stdc++.h"

using namespace std;

const int DI[4] = { 0, 1, 0, -1 };
const int DJ[4] = { 1, 0, -1, 0 };

const int R = 200;
const int C = 150;

int main() {
	vector<string> grid(R, string(C, '?'));
	int ci = -1, cj = -1;
	for (int i = 0; i < R; ++i) {
		string line;
		getline(cin, line);	
		while (line.length() < C) {
			line += ' ';
		}
		for (int j = 0; j < C; ++j) {
			grid[i][j] = line[j];
			if (grid[i][j] == '.' && ci == -1) {
				ci = i, cj = j;
			}
		}
	}
	string blank, steps;
	getline(cin, blank);
	getline(cin, steps);
	int d = 0;
	auto move = [&](int s) {
		while (s--) {
			int to_i = (ci + DI[d] + R) % R, to_j = (cj + DJ[d] + C) % C;
			while (grid[to_i][to_j] == ' ') {
				to_i = (to_i + DI[d] + R) % R;
				to_j = (to_j + DJ[d] + C) % C;
			}
			if (grid[to_i][to_j] == '#') {
				break;
			}
			assert(grid[to_i][to_j] != '#' && grid[to_i][to_j] != ' ');
			grid[ci][cj] = ">v<^"[d];
			ci = to_i, cj = to_j;
		}
	};
	int current = 0;
	for (char c : steps) {
		if (c == 'L' || c == 'R') {
			// 歩く！
			move(current);
			// 方向調整
			if (c == 'L') {
				d = (d + 3) % 4;
			} else {
				d = (d + 1) % 4;
			}
			// リセット
			current = 0;
		} else {
			current *= 10;
			current += (c - '0');
		}
	}
	// v classic mistake from me, oh well
	if (current != 0) {
		move(current);
	}
	cout << 1000 * (ci + 1) + 4 * (cj + 1) + d << '\n';
}