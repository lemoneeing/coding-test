import sys
import math

input = sys.stdin.readline

def solution():
    X, Y, D, T = map(int, input().split())
    dist = math.hypot(X, Y)

    ans = dist  # 걷기만

    # 점프 1회 거리가 도달거리보다 길 경우
    if dist < D:
        # 점프 1회 후 되돌아 걷기
        ans = min(ans, T + (D - dist))
        
        # 점프 2회: 각도 조절(=점프로 목적지가 아닌 다른 방향으로 점프 후 다시 목적지 방향으로 점프)로 정확히 도달 가능
        ans = min(ans, 2 * T)

    # 점프 1회 거리가 도달거리보다 짧거나 같은 경우
    else:
        k = int(dist // D)
        
        # k번 점프 + 나머지 걷기 - 점프로만 도달 가능한 경우까지 포함됨.
        ans = min(ans, k * T + (dist - k * D))

        # (k+1)번 점프만으로 도달(각도 조절)
        ans = min(ans, (k + 1) * T)

    # 허용 오차 1e-9이므로 충분히 출력
    print("{:.10f}".format(ans))

solution()
