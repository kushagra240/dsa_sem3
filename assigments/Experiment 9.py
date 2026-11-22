class Graph:
    def __init__(self, v):
        self.v = v
        self.adj = [[0] * v for _ in range(v)]

    def add_edge(self, u, w, wt):
        self.adj[u][w] = wt
        self.adj[w][u] = wt  # Undirected weighted graph

    def display(self):
        print("\nWeighted Adjacency Matrix:")
        print(" ", *range(self.v))
        for i in range(self.v):
            print(i, self.adj[i])

    def prim(self, start):
        if not (0 <= start < self.v):
            print("Invalid starting vertex.")
            return

        INF = float("inf")
        key = [INF] * self.v
        parent = [-1] * self.v
        in_mst = [False] * self.v
        key[start] = 0

        for _ in range(self.v):
            # 1. Pick unvisited vertex with smallest key
            min_key = INF
            u = -1
            for i in range(self.v):
                if not in_mst[i] and key[i] < min_key:
                    min_key = key[i]
                    u = i

            if u == -1:
                print("Graph is disconnected.")
                print("A spanning tree cannot be formed.")
                return

            in_mst[u] = True

            # 2. Update keys of adjacent unvisited vertices
            for i in range(self.v):
                wt = self.adj[u][i]
                if wt > 0 and not in_mst[i] and wt < key[i]:
                    key[i] = wt
                    parent[i] = u

        # 3. Display MST edges and total cost
        print("\nMinimum Spanning Tree (MST):")
        print("Edge\tWeight")
        total = 0
        for i in range(self.v):
            if parent[i] != -1:
                wt = self.adj[i][parent[i]]
                print(f"{parent[i]} - {i}\t{wt}")
                total += wt
        print("Total Minimum Cost:", total)


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
    print("Enter each edge as: source destination weight")
    print(f"Valid vertices: 0 to {vertices - 1}")
    for i in range(edges):
        u, v, weight = map(int, input(f"Edge {i + 1}: ").split())
        if u < 0 or u >= vertices or v < 0 or v >= vertices:
            print("Invalid vertex number.")
            return
        if u == v:
            print("Self-loops are not accepted in this program.")
            return
        if weight <= 0:
            print("Edge weight must be positive.")
            return
        graph.add_edge(u, v, weight)
    graph.display()
    start = int(input("\nEnter starting vertex for Prim's algorithm: "))
    graph.prim(start)


if __name__ == "__main__":
    main()