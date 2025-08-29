import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    tree = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u, v, w = map(int, input().split())
        tree[u].append((v, w))
        tree[v].append((u, w))

    print(tree)

solution()
