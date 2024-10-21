import sys

def solution():
    R, C = map(int, sys.stdin.readline().strip().split())
    treasure_map = []
    for _ in range(R):
        treasure_map.append(list(sys.stdin.readline().strip()))
        print(treasure_map[-1])


solution()