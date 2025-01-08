import sys
input = sys.stdin.readline

def solution():
    C = int(input().strip())
    P = int(input().strip())
    path = [[]]
    for r in range(1, C+1):
        path.append([0]+list(map(int, input().strip().split()))) # 인럽리스트를 사용하려 했지만, 간선이 많을 경우 인접행렬보다 메모리를 많이 사용하게 된다->메모리초과

    plan = []
    visited = [False] * (C+1)
    for tg in map(int, input().strip().split()):
        plan.append(tg)

    ## DFS: 주어진 여행 경로들이 어떻게든 연결되어 있는지 확인하면 됨.
    stack = [plan[0]]
    while stack:
        curr = stack.pop()
        if not visited[curr]:
            visited[curr] = True
            stack.extend([c for c, e in enumerate(path[curr]) if e == 1])

        if all([v for i, v in enumerate(visited) if i in plan]):
            sys.stdout.write("YES")
            return

    sys.stdout.write("NO")

solution()