import sys
from queue import PriorityQueue

input = sys.stdin.readline


def solution():
    N, M = map(int, input().split())
    edges = [[] for _ in range(N+1)]
    for _ in range(M):
        u, v, w = map(int, input().split())
        edges[u].append((w, v))
        edges[v].append((w, u))

    vertexes = [e for e in edges[1]]
    visited = [False] * (N+1)
    visited[1] = True
    min_c = sys.maxsize
    curr_c = 0
    s = 1
    while vertexes:
        cost, e = vertexes[-1]
        if not visited[e]:
            curr_c += cost
            vertexes.pop()
            vertexes.extend(edges[e])
            visited[e] = True
            if e == N:
                min_c = min(min_c, curr_c)
                curr_c -= cost
                visited[s] = False
                visited[e] = False
            else:
                s = e
        else:
            vertexes.pop()


    sys.stdout.write(f"{min_c}")

solution()
