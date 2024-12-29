import sys
input = sys.stdin.readline

def solution():
    C = int(input().strip())
    P = int(input().strip())
    path = [[]]
    for r in range(1, C+1):
        path.append([])
        for c, p in enumerate(list(map(int, input().strip().split()))):
            if p == 1:
                path[r].append(c+1)

    plan = list(map(int, input().strip().split()))

    ## DFS
    stack = [plan[0]]
    visited = [False] * (C+1)
    visited[0] = True

    while stack:
        curr = stack.pop()
        if not visited[curr]:
            visited[curr] = True
            stack.extend(path[curr])

        if all(visited):
            print("YES")
            return

    print("NO")

solution()
