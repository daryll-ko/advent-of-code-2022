#include "bits/stdc++.h"

using namespace std;

const int DI[4] = { 0, -1, 0, 1 };
const int DJ[4] = { 1, 0, -1, 0 };

map<char, int> to_index = {
	{'R', 0},
	{'U', 1},
	{'L', 2},
	{'D', 3}
};

int distance(int hi, int hj, int ti, int tj) {
	return max(abs(hi - ti), abs(hj - tj));
}

int main() {
	set<pair<int, int>> tail_positions;
	tail_positions.emplace(0, 0);
	pair<int, int> knots[10]; // head .. .. tail
	for (int i = 0; i < 10; ++i) {
		knots[i] = {0, 0};
	}
	for (int _ = 0; _ < 2000; ++_) {
		char direction;
		int steps;
		cin >> direction >> steps;
		int d = to_index[direction];
		for (int k = 0; k < steps; ++k) {
			int ci_next, cj_next;
			for (int i = 0; i < 9; ++i) {
				if (i == 0) {
					ci_next = knots[i].first + DI[d], cj_next = knots[i].second + DJ[d];
				}
				int old_i = knots[i].first, old_j = knots[i].second;
				knots[i].first = ci_next, knots[i].second = cj_next;
				if (distance(ci_next, cj_next, knots[i + 1].first, knots[i + 1].second) == 2) {
					if (abs(ci_next - knots[i + 1].first) == 2) {
						ci_next = (ci_next + knots[i + 1].first) / 2;
						if (abs(cj_next - knots[i + 1].second) == 2) {
							cj_next = (cj_next + knots[i + 1].second) / 2;
						}
					} else {
						cj_next = (cj_next + knots[i + 1].second) / 2;
						if (abs(ci_next - knots[i + 1].first) == 2) {
							ci_next = (ci_next + knots[i + 1].first) / 2;
						}
					}
				} else {
					ci_next = knots[i + 1].first, cj_next = knots[i + 1].second;
				}
			}
			knots[9].first = ci_next, knots[9].second = cj_next;
			tail_positions.emplace(knots[9].first, knots[9].second);
		}
	}
	cout << tail_positions.size() << '\n';
}