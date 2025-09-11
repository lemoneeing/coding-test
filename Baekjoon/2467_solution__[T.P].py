import sys
input = sys.stdin.readline

def solution():
    N = int(input().strip())
    solutions = list(map(int, input().split()))

    s = 0
    e = N-1
    ans = sys.maxsize
    ss = ee = 0
    while s < e:

        mix = solutions[s] + solutions[e]
        if abs(ans) > abs(mix):
            ans = mix
            ss = s
            ee = e

        # m = (s + e) // 2
        # if s == m or e == m:
        #     break
        if mix < 0:
            s = s+1
        elif mix > 0:
            e = e-1
        else:
            ss = s
            ee = e
            break

    sys.stdout.write(f"{solutions[ss]} {solutions[ee]}")

solution()