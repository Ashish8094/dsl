from collections import deque

def bfs(n, m, edges, start):
    adj = [[] for _ in range(n + 1)]
    
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    visited = [False] * (n + 1)
    queue = deque()

    visited[start] = True
    queue.append(start)

    print(f"BFS {start}: ", end="")

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in adj[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    print()

if __name__ == "__main__":
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]

    start = int(input("node: "))
    bfs(n, m, edges, start)
