# Social Network Connectivity using an adjacency list and BFS.
# Input: n m, then m friendship pairs u v, then starting user ID (0..n-1).
# Each friendship is treated as undirected.

import sys
from collections import deque

def discover_network(friendships, start):
    n = len(friendships)
    visited = [False] * n
    distance = [-1] * n
    visited[start] = True
    distance[start] = 0
    queue = deque([start])
    traversal = []
    levels = []
    while queue:
        user = queue.popleft()
        traversal.append(user)
        while len(levels) <= distance[user]:
            levels.append([])
        levels[distance[user]].append(user)
        for friend in sorted(friendships[user]):
            if not visited[friend]:
                visited[friend] = True
                distance[friend] = distance[user] + 1
                queue.append(friend)
    return traversal, levels

def main():
    data = list(map(int, sys.stdin.read().split()))
    if len(data) < 2:
        return
    n, m = data[0], data[1]
    if n <= 0 or m < 0 or len(data) < 2 + 2 * m + 1:
        return
    friendships = [[] for _ in range(n)]
    pos = 2
    for _ in range(m):
        u, v = data[pos], data[pos + 1]
        pos += 2
        if 0 <= u < n and 0 <= v < n:
            friendships[u].append(v)
            friendships[v].append(u)
    start_user = data[pos]
    if not 0 <= start_user < n:
        return
    traversal, levels = discover_network(friendships, start_user)
    print("BFS:", " ".join(map(str, traversal)))
    for level_number, users in enumerate(levels):
        print("Level", level_number, ":", " ".join(map(str, users)))

if __name__ == "__main__":
    main()
