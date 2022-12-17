#include "bits/stdc++.h"

using namespace std;

set<int> relevant = {
	20, 60, 100, 140, 180, 220
};

int main() {
	int current_cycle = 0, value = 1, answer = 0;
	auto advance_cycle = [&]() {
		current_cycle += 1;
		if (relevant.count(current_cycle)) {
			answer += current_cycle * value;
		}
	};
	for (int _ = 1; _ <= 143; ++_) {
		string op;
		cin >> op;
		if (op == "noop") {
			advance_cycle();
		} else {
			int add;
			cin >> add;
			advance_cycle();
			advance_cycle();
			value += add;
		}
	}
	cout << answer << '\n';
}