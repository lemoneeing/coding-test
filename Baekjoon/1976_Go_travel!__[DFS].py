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

    plan = []
    visited = {}
    for tg in map(int, input().strip().split()):
        plan.append(tg)
        visited[tg] = False

    ## DFS
    stack = [plan[0]]
    while stack:
        curr = stack.pop()
        if not visited.get(curr, False):
            if curr in visited:
                visited[curr] = True
            stack.extend(path[curr])

        if all(visited.values()):
            sys.stdout.write("YES")
            return

    sys.stdout.write("NO")

solution()
