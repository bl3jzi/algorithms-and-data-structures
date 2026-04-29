# O( V^3 ) time complexity
# O( V^2 ) space complexity
# Works on matrix list
def floyd_warshall(graph):
    n = len(graph)

    dist = [[float('inf')] * n for _ in range(n)]
    parent = [[-1] * n for _ in range(n)]

    for u in range(n): # adjacency list
        dist[u][u] = 0
        for v, w in graph[u]:
            dist[u][v] = w
            parent[u][v] = u

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    parent[i][j] = parent[k][j]

    for i in range(n):
        if dist[i][i] < 0:
            return None

    return dist, parent

def de_graph(graph,distance): # Used when graph is in form: [[0, 2, 0, -1], ...]
    for i in range(len(distance)):
        for j in range(len(distance)):
            if i == j:
                distance[i][j] = 0 # path to itself
            elif graph[i][j] != 0:
                distance[i][j] = graph[i][j]


def reconstruct_path(parent, src, dst):
    if parent[src][dst] == -1:
        return None
    path = []
    cur = dst
    while cur != src:
        path.append(cur)
        cur = parent[src][cur]
    path.append(src)
    return path[::-1]