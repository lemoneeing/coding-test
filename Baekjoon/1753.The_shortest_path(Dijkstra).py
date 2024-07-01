import sys
from queue import PriorityQueue

def solution():
    V, E = map(int, sys.stdin.readline().split())
    K = int(sys.stdin.readline())
    adj = [[] for _ in range(V+1)]
    visited = [False for _ in range(V+1)]
    dist = [sys.maxsize] * (V+1)
    q = PriorityQueue()

    for _ in range(E):
        v, n, w = map(int, sys.stdin.readline().split())
        adj[v].append((n, w))

    q.put((0, K))
    dist[K] = 0

    while q.queue:
        curr = q.get()
        curr_v = curr[1]

        for next in adj[curr_v]:
            if visited[next[0]]:
                continue

            if dist[next[0]] > dist[curr_v] + next[1]:
                dist[next[0]] = dist[curr_v] + next[1]
                q.put((dist[next[0]], next[0]))

        visited[curr_v] = True

    for d in dist[1:]:
        if d < sys.maxsize:
            sys.stdout.write(f"{d}\n")
        else:
            sys.stdout.write("INF\n")

solution()