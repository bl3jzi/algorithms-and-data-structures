# O( V * E ) - time complexity
# O( V + E ) - space complexity
# Works with negative weights

# if graph = [(u,v,w), (u2,v2,w2)...]
# elif graph = [ [ (v,w), (v2,w) ], [ (v,w), ... ]...] then use make_edges
G = [
    [(1, 1), (3, 2)],  # 0 -> 1 (waga 1), 0 -> 3 (waga 2)
    [(2, -1), (4, 2)],  # 1 -> 2 (waga -1), 1 -> 4 (waga 2)
    [(5, -1)],  # 2 -> 5 (waga -1)
    [(2, -1), (6, 3)],  # 3 -> 2 (waga -1), 3 -> 6 (waga 3)
    [(7, 5)],  # 4 -> 7 (waga 5)
    [(6, -2), (8, 4)],  # 5 -> 6 (waga -2), 5 -> 8 (waga 4)
    [],  # 6 - brak krawędzi wychodzących
    [(8, 7)],  # 7 -> 8 (waga 7)
    [(6, 2)]  # 8 -> 6 (waga 2)
]
def make_edges(graph):
    V = len(graph)
    E = []
    for u in range(V):
        for v, w in graph[u]:
            E.append((u, v, w))
    return E

def bellman_ford(graph, root):
    n = len(graph)
    E = make_edges(graph)

    parent = [None for _ in range(n)]
    dist = [float('inf') for _ in range(n)]
    dist[root] = 0

    for i in range(n - 1):
        updated = False
        for u, v, w in E:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                parent[v] = u
                updated = True

        if not updated:
            break

    for u, v, w in E:
        if dist[u] + w < dist[v]:
            print("Negative cycle")
            return None

    return dist, parent

print(bellman_ford(G,0))