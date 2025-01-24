import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    ans = 0
    buildings = []
    for _ in range(n):
        x, y = map(int, input().split())
        if y == 0:
            buildings = []
            continue

        if y not in buildings: # 새로 등장한 높이 = 가장 높거나 가장 낮거나 = 새 건물임 +1
            buildings.append(y)
            ans += 1
        else:
            is_new = False

            idx = len(buildings) - 1 - (buildings[::-1].index(y)) # 현재 높이와 동일한 건물이 있는 지점부터 하나씩 비교
            for h in buildings[idx+1:]:
                if h < y: # 중간에 낮은 높이 건물이 있다면 이번 건물은 새 건물이므로 +1
                    buildings.append(y)
                    ans += 1
                    is_new = True
                    break

            if not is_new: # 중간에 높은 건물만 있다면 이번 건물은 새 건물이 아닐 수 도 있음.
                buildings.remove(y)
                buildings.append(y)

    sys.stdout.write(f"{ans}")

solution()