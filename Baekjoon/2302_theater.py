import sys
input = sys.stdin.readline

def solution():
    N = int(input().strip())
    M = int(input().strip())
    vips = []
    for _ in range(M):
        vips.append(int(input().strip()))

    ans = 1
    e = 0
    for v in range(M+1):
        if v == M:  # 마지막 vip 좌석 ~ 우측 끝 좌석
            if M > 0:
                s = vips[-1] + 1
            else:   # vip 석 없을 경우
                s = 1
            e = N+1
        else:       # 좌측 첫 좌석 ~ vip OR vip 사이
            s = e + 1
            e = vips[v]


        if s < e:
            case = [0] * (e - s + 1)
            case[1] = 1
            if len(case) > 2:
                case[2] = 2
            if e - s >= 3:
                for i in range(3, len(case)):
                    case[i] = case[i - 1] + case[i - 2]

            ans *= case[-1]

    print(ans)

solution()