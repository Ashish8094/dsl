class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            elif self.rank[root_v] < self.rank[root_u]:
                self.parent[root_v] = root_u
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True
        return False

def kruskal(edges, n):
    edges.sort(key=lambda x: x[0])
    dsu = DisjointSet(n)
    
    mst_weight = 0
    mst_edges = []

    for weight, u, v in edges:
        if dsu.union(u, v):
            mst_weight += weight
            mst_edges.append((u, v, weight))

    return mst_weight, mst_edges

n = int(input("Enter number of vertices: "))
m = int(input("Enter number of edges: "))
print("Enter each edge in format : weight u v")

edges = []
for _ in range(m):
    w, u, v = map(int, input().split())
    edges.append((w, u, v))

mst_weight, mst_edges = kruskal(edges, n)
print("Total weight of MST:", mst_weight)
print("Edges in MST:")
for u, v, w in mst_edges:
    print(f"{u} -- {v} == {w}")
