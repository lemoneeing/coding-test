import sys
from heapq import heappush

def solution():
    N, M, X = map(int, sys.stdin.readline().strip().split())
    adj = [[] for _ in range(N+1)]
    for _ in range(M):
        s, e, w = map(int, sys.stdin.readline().strip().split())
        heappush(adj[s], (w, e))

    for i in range(N+1):
        print(f"{i}: {adj[i]}")

solution()