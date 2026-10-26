# Input: n m, then m undirected edges u v, then starting vertex.
# Vertices are 0..n-1. Prints BFS traversal and vertices grouped by distance level.

import sys
from collections import deque

def bfs_levels(graph, start):
    n = len(graph)
    distance = [-1] * n
    distance[start] = 0
    queue = deque([start])
    order = []
    levels = []
    while queue:
        vertex = queue.popleft()
        order.append(vertex)
        while len(levels) <= distance[vertex]:
            levels.append([])
        levels[distance[vertex]].append(vertex)
        for neighbor in sorted(graph[vertex]):
            if distance[neighbor] == -1:
                distance[neighbor] = distance[vertex] + 1
                queue.append(neighbor)
    return order, levels

def main():
    data = list(map(int, sys.stdin.read().split()))
    if len(data) < 2:
        return
    n, m = data[0], data[1]
    if n <= 0 or m < 0 or len(data) < 2 + 2 * m + 1:
        return
    graph = [[] for _ in range(n)]
    index = 2
    for _ in range(m):
        u, v = data[index], data[index + 1]
        index += 2
        if 0 <= u < n and 0 <= v < n:
            graph[u].append(v)
            graph[v].append(u)
    start = data[index]
    if not 0 <= start < n:
        return
    order, levels = bfs_levels(graph, start)
    print("BFS:", " ".join(map(str, order)))
    for i, level in enumerate(levels):
        print("Level", i, ":", " ".join(map(str, level)))

if __name__ == "__main__":
    main()
