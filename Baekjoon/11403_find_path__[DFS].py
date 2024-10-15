import sys

def solution():
    N = int(sys.stdin.readline().strip())
    grp = []
    
    check = []
    visited = []
    adj = []
    for s in range(N):
        grp.append(sys.stdin.readline().strip().split())
        adj.append([])
        check.append([])
        visited.append(False)
        
        for e, v in enumerate(grp[s]):
            if v == '1':
                adj[s].append(e)

    stack = []
    for s in range(N):
        visited[s] = True
        stack.append(adj[s])
        while stack:
            nxt_path = stack.pop()
            for nxt in nxt_path:
                grp[s][nxt] = '1'
                if not visited[nxt]:
                    visited[nxt] = True
                    stack.append(adj[nxt])
        visited = [False] * N
            
    for _ in range(N):
        sys.stdout.write(f"{' '.join(grp[_])}\n")
            
solution()