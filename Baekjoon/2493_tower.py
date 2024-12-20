import sys
input = sys.stdin.readline

def solution():
    N = int(input().strip())
    towers = [int(e) for e in input().strip().split()]
    ans = ['0'] * N

    for i in range(N-1, 0, -1):
        curr_tower = towers.pop(i)
        higher = [t for t in towers if t > curr_tower]
        if higher:
            ans[i] = str(higher[-1])

    sys.stdout.write(f"{' '.join(ans)}")

solution()
