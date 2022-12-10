#include "bits/stdc++.h"

using namespace std;

int main() {
	int current_cycle = 0, value = 1;
	auto advance_cycle = [&]() {
		current_cycle += 1;
		cout << (abs((current_cycle - 1) % 40 - value) <= 1 ? '#' : '.');
		if (current_cycle % 40 == 0) {
			cout << '\n';
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
}