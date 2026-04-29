# O( E * Log V )

from queue import PriorityQueue
def dijkstra(graph,root):
    n = len(graph)
    queue = PriorityQueue()
    queue.put((0,root))

    dist = [float("inf") for _ in range(n)]
    dist[root] = 0

    parent = [-1 for _ in range(n)]

    while not queue.empty():
        dist_u, u = queue.get()

        if dist_u > dist[u]:
            continue

        for v, cost in graph[u]:
            if dist[v] > dist[u] + cost:
                dist[v] = dist[u] + cost
                parent[v] = u
                queue.put((dist[v],v))

    return dist,parent

def print_graph(parent,target):
    result = []
    while target is not None:
        result.append(target)
        target = parent[target]
    return result[::-1]