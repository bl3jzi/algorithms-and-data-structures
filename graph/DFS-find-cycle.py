def has_cycle_directed(graph, n):
    visited = [False] * n
    stack = [False] * n

    def dfs(u):
        visited[u] = True
        stack[u] = True  # we put vertex on stack

        for v in graph[u]:
            if not visited[v]:
                if dfs(v): return True
            elif stack[v]: # neighbor on stack
                return True

        stack[u] = False # remove vertex from stack
        return False

    for i in range(n):
        if not visited[i]:
            if dfs(i): return True
    return False

def has_cycle_undirected(G):
    n = len(G)
    visited = [False] * n

    def dfs(u, parent):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                if dfs(v, u):
                    return True
            elif v != parent:
                return True
        return False

    for u in range(n):
        if not visited[u]:
            if dfs(u, -1):
                return True

    return False

