#include "bits/stdc++.h"

using namespace std;

set<int> relevant = {
	20, 60, 100, 140, 180, 220
};

int main() {
	int current_cycle = 0, value = 1, answer = 0;
	for (int _ = 1; _ <= 143; ++_) {
		string op;
		cin >> op;
		if (op == "noop") {
			current_cycle += 1;
			if (relevant.count(current_cycle)) {
				answer += current_cycle * value;
			}
		} else {
			int add;
			cin >> add;
			current_cycle += 1;
			if (relevant.count(current_cycle)) {
				answer += current_cycle * value;
			}
			current_cycle += 1;
			if (relevant.count(current_cycle)) {
				answer += current_cycle * value;
			}
			value += add;
		}
	}
	cout << answer << '\n';
}