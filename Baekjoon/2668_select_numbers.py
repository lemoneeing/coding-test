import sys

def solution():
    N = int(sys.stdin.readline().strip())
    g = [[] for _ in range(N+1)]
    visited = [False]
    ans = []
    for _ in range(N):
        g[int(sys.stdin.readline().strip())].append(_+1)
        visited.append(False)

    def dfs(node, route):
        nonlocal ans, visited
        visited[node] = True
        route.append(node)

        if len(g[node]) > 0:
            for next in g[node]:
                if next not in route:
                    dfs(next, route.copy())
                else:
                    ans.extend(route)
                    return

    for i in range(1, N+1):
        if not visited[i]:
            dfs(i, [])

    sys.stdout.write(f"{len(ans)}\n")
    for e in ans:
        sys.stdout.write(f"{e}\n")

solution()