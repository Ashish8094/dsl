#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    vector<vector<int>> adj(n + 1, vector<int>(n + 1, 0));

    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        adj[u][v] = 1;
        adj[v][u] = 1;  
    }
    int start;
    cout << "Start node: ";
    cin >> start;

    vector<bool> visited(n + 1, false);
    stack<int> s;

    s.push(start);

    cout << "DFS " << start << ": ";

    while (!s.empty()) {
        int node = s.top();
        s.pop();

        if (!visited[node]) {
            cout << node << " ";
            visited[node] = true;

            for (int neighbor = n; neighbor >= 1; neighbor--) {
                if (adj[node][neighbor] == 1 && !visited[neighbor]) {
                    s.push(neighbor);
                }
            }
        }
    }
    cout << "\n";
    return 0;
}