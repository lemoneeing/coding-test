import sys
input = sys.stdin.readline

def solution():
    sensors_cnt = int(input())
    bts_cnt = int(input())
    sensors = list(map(int, input().split()))
    sensors.sort()

    dist = []
    for f, b in zip(sensors[:-1], sensors[1:]):
        dist.append(b-f)
    dist.sort()

    print(sum(dist[:sensors_cnt - bts_cnt]))

solution()
