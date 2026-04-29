from collections import deque
# O( V + E )

def BFS(graph: list,root: int):
    n = len(graph)
    Q = deque()

    visited = [False for _ in range(n)]
    dist = [float("inf") for _ in range(n)]

    visited[root] = True
    dist[root] = 0
    res = root
    Q.append(root)

    result = []

    while Q:
        u = Q.popleft()
        result.append(u)              # (graph expanding history)
        if dist[u] > dist[res]:       # finding the furthest vertex
            res = u
                                      # for matrix version
        for v in graph[u]:            # for v in range(len(graph_matrix)):
            if not visited[v]:        #    if not visited[v] and graph_m[u][v] == 1:

                visited[v] = True
                dist[v] = dist[u] + 1
                Q.append(v)

    return res, dist, result


