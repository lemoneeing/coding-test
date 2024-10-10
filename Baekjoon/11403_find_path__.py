import sys

def solution():
    N = int(sys.stdin.readline().strip())
    grp = []
    
    check = []
    adj = []
    for s in range(N):
        grp.append(sys.stdin.readline().strip().split())
        adj.append([])
        check.append([])
        
        for e, v in enumerate(grp[s]):
            if v == '1':
                adj[s].append(e)
    
    
    for start in range(N):
        stack = [n for n in adj[start]]
        while stack:
            next = stack.pop()
            
            if next not in check[start]:
                grp[start][next] = '1'
            
            check[start].extend(adj[next])
            
            for n in adj[next]:
                if (q and q[-1] != n) or n not in check[start]:
                    q.append(n)
            
    for _ in range(N):
        sys.stdout.write(f"{' '.join(grp[_])}\n")
            
solution()