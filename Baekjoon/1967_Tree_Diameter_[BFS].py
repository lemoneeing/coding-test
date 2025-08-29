import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    tree = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u, v, w = map(int, input().split())
        tree[u].append((v, w))
        tree[v].append((u, w))

    # 임의의 한 노드에서 가장 먼 거리의 정점을 찾는다. - DFS
    dist = [-1] * (n+1) # 임의의 노드 1에서 다른 노드까지의 거리 배열. 1은 루트노드라서 다른 모든 정점과 연결되어 있으므로
    dist[1] = 0

    def dfs(start):
        nonlocal dist

        stack = [(start, 0)]
        while stack:
            nxt, w = stack.pop(-1)
            for nd, d in tree[nxt]:
                if dist[nd] < 0:
                    dist[nd] = w + d
                    stack.append((nd, dist[nd]))

    dfs(1)
    tmp = dist.index(max(dist)) # 루트노드에서 가장 먼 거리에 있는 노드 발견

    dist = [-1] * (n+1) # 위에서 찾은 tmp 노드로부터 다른 노드까지의 거리 배열 초기화.
    dist[tmp] = 0
    dfs(tmp)

    sys.stdout.write(f"{max(dist)}")

solution()
