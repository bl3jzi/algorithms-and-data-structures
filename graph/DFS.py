# O( V + E )

def DFS(graph: list,root: int):
    n = len(graph)

    parent = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]

    dist = [float("inf") for _ in range(n)]
    dist[root] = 0

    discovery_time = [0 for _ in range(n)]
    finish_time = [0 for _ in range(n)]

    result = []
    time  = [0]

    def DFSVisit(u):
        visited[u] = True
        time[0] += 1
        discovery_time[u] = time[0]

        for v in graph[u]:
            if not visited[v]:
                parent[v] = u
                dist[v] = dist[u] + 1
                DFSVisit(v)

        result.append(u)
        time[0] += 1
        finish_time[u] = time[0]

    DFSVisit(root)

    for i in range(n):
        if not visited[i]:
            DFSVisit(i)

    return dist