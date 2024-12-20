import sys
input = sys.stdin.readline

def solution():
    N = int(input().strip())
    towers = [int(e) for e in input().strip().split()]

    sys.stdout.write(f"0 ")
    s = [towers[0]]
    for i in range(1, N):
        curr = towers[i]
        while s and curr > s[-1]:
            s.pop()
        if s:
            sys.stdout.write(f"{towers.index(s[-1]) + 1} ")
        else:
            sys.stdout.write(f"0 ")
        s.append(curr)

solution()
