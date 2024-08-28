# 11437 기본으로 풀려고 했으나 93% 에서 시간초과

import sys
from collections import deque

def bfs(graph, start):
    p = [0] * (len(graph))
    d = [0] * (len(graph))

    q = deque()
    q.append(start)
    d[start] = 0
    while q:
        curr = q.popleft()

        for c in graph[curr]:
            graph[c].remove(curr)
            p[c] = curr
            d[c] = d[curr] + 1
            q.append(c)

    return p, d

def solution():
    N = int(sys.stdin.readline())
    g = [[] for _ in range(N+1)]
    for _ in range(N-1):
        s, e = map(int, sys.stdin.readline().split())
        g[s].append(e)
        g[e].append(s)

    # 그래프 탐색: 깊이, 부모 찾기
    parent, depth = bfs(g, 1)

    def lca(node1, node2):
        nonlocal parent, depth

        # 깊이 맞추기
        while depth[node1] != depth[node2]:
            if depth[node1] > depth[node2]:
                node1 = parent[node1]
            else:
                node2 = parent[node2]

        # 한 쪽이 다른 쪽의 부모일 때
        if node1 == node2:
            return node1

        # 동일한 깊이의 서로 다른 node 에서 시작
        while parent[node1] != parent[node2]:
            node1 = parent[node1]
            node2 = parent[node2]

        if parent[node1] != parent[node2]:
            return -1
        else:
            return parent[node1]

    M = int(sys.stdin.readline())
    for _ in range(M):
        n1, n2 = map(int, sys.stdin.readline().split())
        sys.stdout.write(f"{lca(n1, n2)}\n")

solution()