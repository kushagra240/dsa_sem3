# Road Network Exploration using DFS and an adjacency matrix.
# Input: n, n*n matrix values, then starting location (0..n-1).
# 1/non-zero means a road exists between two locations.

import sys

def explore_roads(road_matrix, start):
    n = len(road_matrix)
    visited = [False] * n
    route = []
    stack = [start]
    while stack:
        location = stack.pop()
        if visited[location]:
            continue
        visited[location] = True
        route.append(location)
        for neighbor in range(n - 1, -1, -1):
            if road_matrix[location][neighbor] != 0 and not visited[neighbor]:
                stack.append(neighbor)
    return route

def main():
    values = list(map(int, sys.stdin.read().split()))
    if not values:
        return
    n = values[0]
    if n <= 0 or len(values) < 1 + n * n + 1:
        return
    raw = values[1:1 + n * n]
    road_matrix = [raw[i * n:(i + 1) * n] for i in range(n)]
    start = values[1 + n * n]
    if start < 0 or start >= n:
        return
    print("DFS:", " ".join(map(str, explore_roads(road_matrix, start))))

if __name__ == "__main__":
    main()
