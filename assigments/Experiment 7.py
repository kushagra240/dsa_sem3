class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.v = vertices
        self.adj = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, w):
        self.adj[u][w] = 1
        self.adj[w][u] = 1  # Undirected graph

    def display(self):
        print("\nAdjacency Matrix:")
        print(" ", *range(self.vertices))
        for i in range(self.vertices):
            print(i, self.adj[i])

    def dfs(self, start):
        if not (0 <= start < self.v):
            print("Invalid starting vertex.")
            return []

        visited = [False] * self.v
        order = []

        def explore(u):
            visited[u] = True
            order.append(u)
            for nb in range(self.v):
                if self.adj[u][nb] == 1 and not visited[nb]:
                    explore(nb)

        explore(start)
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
    start = int(input("\nEnter starting vertex for DFS: "))
    traversal = graph.dfs(start)
    if traversal:
        print("DFS Traversal:", " -> ".join(map(str, traversal)))
        unreachable = [v for v in range(vertices) if v not in traversal]
        if unreachable:
            print("Unreachable vertices:", *unreachable)


if __name__ == "__main__":
    main()