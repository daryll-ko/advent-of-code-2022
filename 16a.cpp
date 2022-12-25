#include "bits/stdc++.h"

using namespace std;

const int V = 51;
const int TIME = 30;
const int INF = 123'456'789;

int main() {
	// Let's pretend I never thought of this as an MCF problem ahahaha...
	map<string, int> to_index;
	int index = 0, to_flow_rate[V];
	vector<int> relevant; // indices with flow_rate > 0
	int index_in_relevant[V];
	vector<vector<int>> g(V);
	for (int i = 0; i < V; ++i) {
		to_flow_rate[i] = 0;
		index_in_relevant[i] = -1;
	}
	for (int _ = 0; _ < V; ++_) {
		string S;
		int flow_rate;
		cin >> S >> flow_rate;
		if (!to_index.count(S)) {
			to_index[S] = index++;
		}
		if (flow_rate > 0) {
			index_in_relevant[to_index[S]] = (int)relevant.size();
			relevant.push_back(to_index[S]);
			to_flow_rate[to_index[S]] = flow_rate;
		}
		int outdegree;
		cin >> outdegree;
		while (outdegree--) {
			string T;
			cin >> T;
			if (!to_index.count(T)) {
				to_index[T] = index++;
			}
			g[to_index[S]].push_back(to_index[T]);
		}
	}
	int M = (int)relevant.size();
	int dp[V][1 << M][TIME + 1]; // (last visited, opened valves, time passed) -> maximum pressure
	for (int i = 0; i < V; ++i) {
		for (int j = 0; j < 1 << M; ++j) {
			for (int k = 0; k <= TIME; ++k) {
				dp[i][j][k] = -INF;
			}
		}
	}
	dp[to_index["AA"]][0][0] = 0;
	auto compute_pressure = [&](int open) {
		int answer = 0;
		for (int l = 0; l < M; ++l) {
			if ((open & (1 << l)) > 0) {
				answer += to_flow_rate[relevant[l]];
			}
		}
		return answer;
	};
	for (int k = 1; k <= TIME; ++k) {
		for (int i = 0; i < V; ++i) {
			for (int j = 0; j < 1 << M; ++j) {
				if (index_in_relevant[i] != -1 && (j & (1 << index_in_relevant[i])) > 0) {
					dp[i][j][k] = max(
						dp[i][j][k],
						compute_pressure(j & ~(1 << index_in_relevant[i])) +
							dp[i][j & ~(1 << index_in_relevant[i])][k - 1]
					);
				}
				for (int t : g[i]) {
					dp[i][j][k] = max(dp[i][j][k], compute_pressure(j) + dp[t][j][k - 1]);
				}
			}
		}
	}
	int answer = 0;
	for (int i = 0; i < V; ++i) {
		for (int j = 0; j < 1 << M; ++j) {
			for (int k = 0; k <= TIME; ++k) {
				answer = max(answer, dp[i][j][k]);
			}
		}
	}
	cout << answer << '\n';
}