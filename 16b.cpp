#include "bits/stdc++.h"

using namespace std;

const int V = 51;
const int TIME = 5;
const int INF = 123'456'789;

int main() {
	// what an AoC problem!

	unordered_map<string, int> to_index;
	vector<int> relevant; // indices with flow_rate > 0
	int index = 0, to_flow_rate[V], index_in_relevant[V];
	vector<int> g[V];

	// parse input
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

	// dp setup
	int dp[V][V][1 << M]; // (me, elephant, opened valves) -> maximum pressure [time is implicit later on]
	for (int i1 = 0; i1 < V; ++i1) {
		for (int i2 = 0; i2 < V; ++i2) {
			for (int j = 0; j < 1 << M; ++j) {
				dp[i1][i2][j] = -INF;
			}
		}
	}
	dp[to_index["AA"]][to_index["AA"]][0] = 0;

	// pressure computation
	int compute_pressure_memo[1 << M];
	for (int i = 0; i < 1 << M; ++i) {
		compute_pressure_memo[i] = 0;
		for (int j = 0; j < M; ++j) {
			if ((i & (1 << j)) > 0) {
				compute_pressure_memo[i] += to_flow_rate[relevant[j]];
			}
		}
	}

	for (int k = 1; k <= TIME; ++k) {
		// setup
		int new_dp[V][V][1 << M];
		for (int i1 = 0; i1 < V; ++i1) {
			for (int i2 = 0; i2 < V; ++i2) {
				for (int j = 0; j < 1 << M; ++j) {
					new_dp[i1][i2][j] = -INF;
				}
			}
		}

		// transitions
		for (int i1 = 0; i1 < V; ++i1) {
			for (int i2 = 0; i2 < V; ++i2) {
				for (int j = 0; j < 1 << M; ++j) {
					// both moved
					for (int t1 : g[i1]) {
						for (int t2 : g[i2]) {
							new_dp[i1][i2][j] = max(new_dp[i1][i2][j], compute_pressure_memo[j] + dp[t1][t2][j]);
						}
					}

					// I moved
					if (index_in_relevant[i2] != -1 && (j & (1 << index_in_relevant[i2])) > 0) {
						for (int t1 : g[i1]) {
							new_dp[i1][i2][j] = max(
								new_dp[i1][i2][j], 
								compute_pressure_memo[j & ~(1 << index_in_relevant[i2])] +
									dp[t1][i2][j & ~(1 << index_in_relevant[i2])]
							);
						}
					}

					// elephant moved
					if (index_in_relevant[i1] != -1 && (j & (1 << index_in_relevant[i1])) > 0) {
						for (int t2 : g[i2]) {
							new_dp[i1][i2][j] = max(
								new_dp[i1][i2][j], 
								compute_pressure_memo[j & ~(1 << index_in_relevant[i1])] +
									dp[i1][t2][j & ~(1 << index_in_relevant[i1])]
							);
						}
					}

					// both stayed, at same valve
					if (i1 == i2 && index_in_relevant[i1] != -1 && (j & (1 << index_in_relevant[i1])) > 0) {
						new_dp[i1][i2][j] = max(
							new_dp[i1][i2][j],
							compute_pressure_memo[j & ~(1 << index_in_relevant[i1])] +
								dp[i1][i2][j & ~(1 << index_in_relevant[i1])]
						);
					}

					// both stayed, at different valves
					if (
						i1 != i2 && index_in_relevant[i1] != -1 && index_in_relevant[i2] != -1 &&
						(j & (1 << index_in_relevant[i1])) > 0 && (j & (1 << index_in_relevant[i2])) > 0
						) {
						new_dp[i1][i2][j] = max(
							new_dp[i1][i2][j],
							compute_pressure_memo[j & ~(1 << index_in_relevant[i1]) & ~(1 << index_in_relevant[i2])] +
								dp[i1][i2][j & ~(1 << index_in_relevant[i1]) & ~(1 << index_in_relevant[i2])]
						);
					}
				}
			}
		}

		// update
		for (int i1 = 0; i1 < V; ++i1) {
			for (int i2 = 0; i2 < V; ++i2) {
				for (int j = 0; j < 1 << M; ++j) {
					dp[i1][i2][j] = new_dp[i1][i2][j];
				}
			}
		}
	}

	// extracting answer
	int answer = 0;
	for (int i1 = 0; i1 < V; ++i1) {
		for (int i2 = 0; i2 < V; ++i2) {
			for (int j = 0; j < 1 << M; ++j) {
				answer = max(answer, dp[i1][i2][j]);
			}
		}
	}
	cout << answer << '\n';
}