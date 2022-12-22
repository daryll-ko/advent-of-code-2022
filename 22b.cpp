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
	int cd = 0;
	auto transform = [&](int i, int j, int d) { // pain
		if (i == 0 && j / 50 == 1 && d == 3) {
			return make_tuple(150 + (j - 50), 0, 0);
		} else if (i == 0 && j / 50 == 2 && d == 3) {
			return make_tuple(199, j - 100, 3);
		} else if (j == 50 && i / 50 == 0 && d == 2) {
			return make_tuple(149 - i, 0, 0);
		} else if (j == 149 && i / 50 == 0 && d == 0) {
			return make_tuple(149 - i, 99, 2);
		} else if (i == 49 && j / 50 == 2 && d == 1) {
			return make_tuple(50 + (j - 100), 99, 2);
		} else if (j == 50 && i / 50 == 1 && d == 2) {
			return make_tuple(100, i - 50, 1);
		} else if (j == 99 && i / 50 == 1 && d == 0) {
			return make_tuple(49, 100 + (i - 50), 3);
		} else if (i == 100 && j / 50 == 0 && d == 3) {
			return make_tuple(50 + j, 50, 0);
		} else if (j == 0 && i / 50 == 2 && d == 2) {
			return make_tuple(49 - (i - 100), 50, 0);
		} else if (j == 99 && i / 50 == 2 && d == 0) {
			return make_tuple(49 - (i - 100), 149, 2);
		} else if (i == 149 && j / 50 == 1 && d == 1) {
			return make_tuple(150 + (j - 50), 49, 2);
		} else if (j == 0 && i / 50 == 3 && d == 2) {
			return make_tuple(0, 50 + (i - 150), 1);
		} else if (j == 49 && i / 50 == 3 && d == 0) {
			return make_tuple(149, 50 + (i - 150), 3);
		} else if (i == 199 && j / 50 == 0 && d == 1) {
			return make_tuple(0, 100 + j, 1);
		} else {
			return make_tuple(i + DI[d], j + DJ[d], d);
		}
	};
	auto move = [&](int s) {
		while (s--) {
			auto [to_i, to_j, next_d] = transform(ci, cj, cd);
			if (grid[to_i][to_j] == '#') {
				break;
			}
			grid[ci][cj] = ">v<^"[cd];
			ci = to_i, cj = to_j, cd = next_d;
		}
	};
	int current = 0;
	for (char c : steps) {
		if (c == 'L' || c == 'R') {
			// 歩く！
			move(current);
			// 方向調整
			if (c == 'L') {
				cd = (cd + 3) % 4;
			} else {
				cd = (cd + 1) % 4;
			}
			// リセット
			current = 0;
		} else {
			current *= 10;
			current += (c - '0');
		}
	}
	if (current != 0) {
		move(current);
	}
	cout << 1000 * (ci + 1) + 4 * (cj + 1) + cd << '\n';
}