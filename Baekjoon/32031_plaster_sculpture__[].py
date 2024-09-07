import sys

def solution():

    h, w = map(int, sys.stdin.readline().split())
    cyld = []
    for _ in h:
        cyld.append(list(sys.stdin.readline()))

    # 원기둥 수직으로만 구성 OOOO...
    # O[w][h] = o[w][h-1]+(2*w) if h > 0 else (2*w)+4

    # 원기둥 회전축 세로 I 로만 구성
    # I[w] = I[w-1] + 2 if w > 0 else 4

    # 원기둥 회전축 가로 H 만
    # H[h] = H[h-1] + 2 ir h > 0 else 4

    # O+I
    # 