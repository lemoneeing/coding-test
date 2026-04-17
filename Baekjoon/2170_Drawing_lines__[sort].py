import sys

input = sys.stdin.readline

def solve():
    N = int(input().strip())
    line_set = [tuple(map(int, input().split())) for _ in range(N)]
    line_set.sort(key=lambda x: (x[0], -1 *x[1]))

    # lines = [] # [[s, e], [s2, e2], ...] 이 때 (s,e)와 (s2, e2) 는 겹치는 부분이 없다.
    # ans = 0
    # for ts, te in line_set:
    #     if len(lines) == 0:
    #         # lines.append([ts, te])
    #         ans = te-ts
    #         continue
            
    #     s, e = lines[-1]

    #     if e < ts:
    #         # lines.append([ts, te])
    #         ans += (te-ts)

    #     if s <= ts <= e:
    #         if e < te:
    #             # lines[-1][-1] = te
    #             ans += (te-e)

    # print(ans)

    s = line_set[0][0]
    e = line_set[0][1]
    ans = e-s
    for ts, te in line_set[1:]:
        if e < ts:
            ans += (te-ts)
            s = ts
            e = te

        if s <= ts <= e:
            if e < te:
                ans += (te-e)
                e = te

    print(ans)

solve()