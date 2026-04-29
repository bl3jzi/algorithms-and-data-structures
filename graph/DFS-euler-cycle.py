def find_euler_cycle(graph,root):
    n = len(graph)

    result = []
    clone = [list(vertex) for vertex in graph]

    if not has_eulerian_cycle(graph):
        return []

    def DFSVisit(clone,u):
        nonlocal result

        while clone[u]:
            v = clone[u].pop()
            if u in clone[v]:
                clone[v].remove(u)  # if graph is undirected, we also remove clone[u].remove[v] O( V )
            DFSVisit(clone,v)

        result.append(u)

    DFSVisit(clone,root)

    return result[::-1]

def has_eulerian_cycle(graph):
    for vertex in graph:
        if len(graph[vertex]) % 2 != 0:  # odd degree vertex
            return False
    return True

