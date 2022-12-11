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
	int hi = 0, hj = 0, ti = 0, tj = 0;
	for (int _ = 0; _ < 2000; ++_) {
		char direction;
		int steps;
		cin >> direction >> steps;
		int d = to_index[direction];
		for (int k = 0; k < steps; ++k) {
			int hi_next = hi + DI[d], hj_next = hj + DJ[d];
			if (distance(hi_next, hj_next, ti, tj) == 2) {
				ti = hi, tj = hj;
			}
			hi = hi_next, hj = hj_next;
			tail_positions.emplace(ti, tj);
		}
	}
	cout << tail_positions.size() << '\n';
}