import sys
input = sys.stdin.readline

def solution():
    n, W, L = map(int, input().split())
    trucks = list(map(int, input().split()))
    brg = []
    cost = 0
    while trucks:
        nxt_tr = trucks[0]
        if sum(brg) + nxt_tr <= L:
            brg.append(trucks.pop(0))
            cost += 1
        else:
            cost += (W - len(brg))
            brg.pop(0)

        if not trucks and brg: # 다리에 올라 가지 못한 트럭이 없음.
            cost += W

    sys.stdout.write(f"{cost}")

solution()