import sys

input = sys.stdin.readline

def calculate_max(day, values, amount, holdings):

    if holdings == 0: # 보유한 주식이 없을 땐 (매입, 유지) 중 택 1
        return max(calculate_max(day + 1, values, amount - values[day], holdings + 1),
                   calculate_max(day + 1, values, amount, holdings))

    if day == len(values)-1: # 마지막 날엔 (매매, 유지) 중 택 1
        if amount < 0 < holdings:
            return amount + (values[day] * holdings)
        else:
            return amount

    return max(calculate_max(day + 1, values, amount - values[day], holdings + 1),  # 매입
               calculate_max(day + 1, values, amount + values[day], holdings - 1),  # 매매
               calculate_max(day + 1, values, amount, holdings))                 # 유지


def solution():
    T = int(input().strip())
    for _ in range(T):
        days = int(input().strip())
        expectation = list(map(int, input().split()))

        sys.stdout.write(f"{calculate_max(0, expectation, 0, 0)}\n")

solution()
