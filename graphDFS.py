def dfs(n, m, edges, start):
    adj = [[0] * (n + 1) for _ in range(n + 1)]

    for u, v in edges:
        adj[u][v] = 1
        adj[v][u] = 1

    visited = [False] * (n + 1)
    stack = []

    stack.append(start)

    print(f"DFS {start}: ", end="")

    while stack:
        node = stack.pop()

        if not visited[node]:
            print(node, end=" ")
            visited[node] = True

            for neighbor in range(n, 0, -1):
                if adj[node][neighbor] == 1 and not visited[neighbor]:
                    stack.append(neighbor)
    print()

if __name__ == "__main__":
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    start = int(input("Start node: "))
    dfs(n, m, edges, start)
