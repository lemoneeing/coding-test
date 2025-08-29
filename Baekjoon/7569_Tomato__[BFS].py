import sys
from copy import deepcopy

input = sys.stdin.readline

def solution():
    M, N, H = map(int, input().split())
    floors = []
    for _ in range(H):
        box = []
        for __ in range(N):
            box.append(list(map(int, input().split())))
        floors.append(box)

    print(floors)
    ans = ''


solution()
