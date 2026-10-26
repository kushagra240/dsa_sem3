# Input: n, then n*n adjacency-matrix values, then starting vertex.
# Vertices are 0..n-1. DFS visits neighbors in increasing vertex order.

import sys

def dfs(matrix, start):
    n = len(matrix)
    visited = [False] * n
    order = []
    stack = [start]
    while stack:
        vertex = stack.pop()
        if visited[vertex]:
            continue
        visited[vertex] = True
        order.append(vertex)
        # Reverse push order so the smallest neighbor is visited first.
        for neighbor in range(n - 1, -1, -1):
            if matrix[vertex][neighbor] != 0 and not visited[neighbor]:
                stack.append(neighbor)
    return order

def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    n = data[0]
    needed = 1 + n * n + 1
    if n <= 0 or len(data) < needed:
        return
    flat = data[1:1 + n * n]
    matrix = [flat[i * n:(i + 1) * n] for i in range(n)]
    start = data[1 + n * n]
    if not 0 <= start < n:
        return
    print("DFS:", " ".join(map(str, dfs(matrix, start))))

if __name__ == "__main__":
    main()
