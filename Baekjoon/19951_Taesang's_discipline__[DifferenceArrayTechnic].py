import sys

def solution():
    N, M = map(int, sys.stdin.readline().split())
    h = list(map(int, sys.stdin.readline().split()))
    
    o = [0] * (N+1)
    for _ in range(M):
        s, e, v = map(int, sys.stdin.readline().split())
        o[s-1] += v
        o[e] -= v
        
    for i in range(1, N):
        o[i] += o[i-1]
        
    for j in range(N):
        h[j] += o[j]
    
    sys.stdout.write(f"{' '.join(list(map(str, h)))}")
    
solution()