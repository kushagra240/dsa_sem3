from collections import deque


class Graph:
    def __init__(self, v):
        self.v = v
        self.adj = [[] for _ in range(v)]

    def add_edge(self, u, w):
        self.adj[u].append(w)
        self.adj[w].append(u)  # Undirected graph

    def display(self):
        print("\nAdjacency List:")
        for i in range(self.v):
            print(f"{i} -> {self.adj[i]}")

    def bfs(self, start):
        if not (0 <= start < self.v):
            print("Invalid starting vertex.")
            return []

        visited = [False] * self.v
        visited[start] = True
        q = deque([start])
        order = []

        while q:
            u = q.popleft()
            order.append(u)
            for nb in sorted(self.adj[u]):
                if not visited[nb]:
                    visited[nb] = True
                    q.append(nb)

        return order


def main():
    vertices = int(input("Enter number of vertices: "))
    if vertices <= 0:
        print("Number of vertices must be greater than zero.")
        return
    edges = int(input("Enter number of edges: "))
    if edges < 0:
        print("Number of edges cannot be negative.")
        return
    graph = Graph(vertices)
    print("Enter each edge as source and destination (0 to", vertices - 1, "):")
    for i in range(edges):
        u, v = map(int, input(f"Edge {i + 1}: ").split())
        if u < 0 or u >= vertices or v < 0 or v >= vertices:
            print("Invalid edge. Please enter valid vertex numbers.")
            return
        graph.add_edge(u, v)
    graph.display()
    start = int(input("\nEnter starting vertex for BFS: "))
    traversal = graph.bfs(start)
    if traversal:
        print("BFS Traversal:", " -> ".join(map(str, traversal)))
        unreachable = [v for v in range(vertices) if v not in traversal]
        if unreachable:
            print("Unreachable vertices:", *unreachable)


if __name__ == "__main__":
    main()