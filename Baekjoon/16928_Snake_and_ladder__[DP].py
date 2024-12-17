import sys
from heapq import heappush

input = sys.stdin.readline

def solution():
    L, S = map(int, input().split())
    path = []
    snakes = []
    ladders = []
    for _ in range(L+S):
        heappush(path, tuple(map(int, input().split())))
        if path[-1][0] < path[-1][1]:
            heappush(ladders, path[-1])
        else:
            heappush(snakes, path[-1])
    dp = []
    print(path)
    print(snakes)
    print(ladders)

solution()