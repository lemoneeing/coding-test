import sys
input = sys.stdin.readline


def switch_bulb(bulb_list, to_be, cnt):
    for i in range(1, len(bulb_list)):
        if bulb_list[i-1] != to_be[i-1]:
            bulb_list[i - 1:i + 2] = [1 - e for e in bulb_list[i - 1:i + 2]]

            cnt += 1

    if bulb_list == to_be:
        return cnt
    else:
        return -1


def solution():
    N = int(input())
    bulbs = list(map(int, input().strip()))
    to_be = list(map(int, input().strip()))

    # 처음 스위치 누르고 탐색
    bulbs_switch_zero = [n for n in bulbs]
    bulbs_switch_zero[:2] = [1-e for e in bulbs[:2]]
    turn_switch_from_zero = switch_bulb(bulbs_switch_zero, to_be, 1)

    # 처음 스위치 안누르고 탐색
    bulbs_switch_one = [n for n in bulbs]
    turn_switch_from_one = switch_bulb(bulbs_switch_one, to_be, 0)

    if turn_switch_from_zero >= 0 and turn_switch_from_one >= 0:
        sys.stdout.write(f"{min(turn_switch_from_zero, turn_switch_from_one)}")
    else:
        if turn_switch_from_zero < 0 and turn_switch_from_one < 0:
            sys.stdout.write(f"-1")
        else:
            sys.stdout.write(f"{turn_switch_from_zero if turn_switch_from_zero >= 0 else turn_switch_from_one}")


solution()