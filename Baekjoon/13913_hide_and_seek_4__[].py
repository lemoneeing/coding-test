import sys

def solution():
    s, e = map(int, sys.stdin.readline().split())

    v = [False for _ in range(200001)]

    
    def bfs(curr, path):
        nonlocal v, e
        
        if v[curr] or curr < 0 or curr > 200000:
            return
        
        if curr == e:
            return path
            
        v[curr] = True
    
        for next in (curr-1, curr+1, curr*2):
            if next == curr:
                continue
            
            p = bfs(next, path + [next])
            if p and p[-1] == e:
                return p
        v[curr] = False
        
    ans = bfs(s, [s])
    sys.stdout.write(f"{len(ans)}\n{' '.join(ans)}")
    
solution()