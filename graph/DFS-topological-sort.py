# O(V + E)
# Used only if there is no cycle / Directed Acyclic Graph (DAG)
def DFS(graph,root):
    n = len(graph)
    visited = [False for _ in range(n)]
    result = []

    def DFSVisit(u):
        visited[u] = True

        for v in graph[u]:
            if not visited[v]:
                DFSVisit(v)
        result.append(u)

    DFSVisit(root)

    for i in range(n):
        if not visited[i]:
            DFSVisit(i)

    return result[::-1]
