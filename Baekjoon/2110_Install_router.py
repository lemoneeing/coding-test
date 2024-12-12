import sys

input = sys.stdin.readline

def solution():
    H, R = map(int, input().strip().split())
    houses = []
    for _ in range(H):
        houses.append(int(input().strip()))
    houses.sort()

    # 1. 공유기를 최대한 멀리 설치
    #   멀리 설치하려면?

    # 2. 그 중 가장 가까운 거리는?
    installed = []
    adj = []
    longest = 0
    def install(idx, installable):
        nonlocal R, houses, installed, longest

        if len(installed) == R:
            return

        if installable:
            if installed:
                currDist = abs(installed[-1] - houses[idx])
                if currDist > longest:
                    longest = currDist

            installed.append(houses[idx])

        return max(install(idx + 1, True), install(idx + 1, False)))

    for h in houses:
        install(h)
        install()

