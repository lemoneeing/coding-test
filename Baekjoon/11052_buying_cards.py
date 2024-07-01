import sys

def solution():
    goal = int(sys.stdin.readline())
    packs = [0] + list(map(int, sys.stdin.readline().split()))

    # 목표치 = 2
    for g in range(1, goal+1):
        for i in range(1, g+1):
            if g-i >= 0:
                packs[g] = max(packs[g-i] + packs[i], packs[g])

    sys.stdout.write(f"{packs[goal]}")

solution()