import sys

input = sys.stdin.readline

def check_durability(dub, pos, zero_dub, limit):
    dub[pos] -= 1
    if dub[pos] == 0:
        zero_dub += 1
        return zero_dub == limit

def solution():
    N, K = map(int, input().split())
    dub = list(map(int, input().split()))
    robots = [0] * (2*N)
    while dub.count(0) < K:
        # 로봇 올리기
        if dub[0] > 0 and robots[0] == 0:
            robots[0] = 1
            if check_durability(dub, 0, dub.count(0), K):
                return 3

        # 로봇 내리기
        if robots[N-1] == 1:
            robots[N-1] -= 1

        # 로봇 이동
        for curr, r in enumerate(robots):
            prv = 2 * N - 1 if curr == 0 else curr - 1
            nxt = 0 if curr == 2 * N - 1 else curr + 1

            if robots[nxt] == 0 and dub[nxt] > 0:
                robots[nxt] += 1
                robots[prv] -= 1
                if check_durability(dub, curr, dub.count(0), K):
                    print(2)

            if robots[prev] == 0:
                robots[i] = 1








    ans = ''


solution()
