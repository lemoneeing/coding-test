import sys
input = sys.stdin.readline

def switch_bulb(bulb_list, i):
    if i > 0:
        bulb_list[i - 1:i + 2] = [1 - e for e in bulb_list[i - 1:i + 2]]
    else:
        bulb_list[i:i + 2] = [1 - e for e in bulb_list[i:i + 2]]

def solution():
    N = int(input())
    bulbs = list(map(int, input().strip()))
    to_be = list(map(int, input().strip()))

    # 처음 스위치 누르고 탐색
    bulbs_switch_zero = [n for n in bulbs]
    turn_switch_from_zero = 1
    switch_bulb(bulbs_switch_zero, 0)
    for i in range(1, N):
        if bulbs_switch_zero[i-1] != to_be[i-1]:
            switch_bulb(bulbs_switch_zero, i)
            turn_switch_from_zero += 1

    # 처음 스위치 안누르고 탐색
    bulbs_switch_one = [n for n in bulbs]
    turn_switch_from_one = 0
    for i in range(1, N):
        if bulbs_switch_one[i-1] != to_be[i-1]:
            switch_bulb(bulbs_switch_one, i)
            turn_switch_from_one += 1

    if bulbs_switch_zero == to_be and bulbs_switch_one == to_be:
        sys.stdout.write(f"{min(turn_switch_from_zero, turn_switch_from_one)}")
    else:
        if bulbs_switch_zero != to_be and bulbs_switch_one == to_be:
            sys.stdout.write(f"{turn_switch_from_one}")
        elif bulbs_switch_zero == to_be and bulbs_switch_one != to_be:
            sys.stdout.write(f"{turn_switch_from_zero}")
        else:
            sys.stdout.write(f"-1")

solution()