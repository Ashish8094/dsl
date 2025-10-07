#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    vector<int> adj[n + 1]; 

    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;

        adj[u].push_back(v);
        adj[v].push_back(u);  
    }

    int start;
    cout << "node: ";
    cin >> start;

    vector<bool> visited(n + 1, false);
    queue<int> q;

    visited[start] = true;
    q.push(start);

    cout << "BFS " << start << ": ";

    while (!q.empty()) {
        int node = q.front();
        q.pop();

        cout << node << " ";

        for (int neighbor : adj[node]) {
            if (!visited[neighbor]) {
                visited[neighbor] = true;
                q.push(neighbor);
            }
        }
    }
    cout << "\n";
    return 0;
}
