n = int(input())

graph = []

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

start = int(input())

visited = [False] * n
queue = [start]
visited[start] = True

while queue:
    vertex = queue.pop(0)
    print(vertex, end=" ")

    for i in range(n):
        if graph[vertex][i] == 1 and not visited[i]:
            visited[i] = True
            queue.append(i)
