import sys
from copy import deepcopy

input = sys.stdin.readline

EGG_CNT = 0
broken_cnt = 0


def hit(eggs, att_i, broken):
    global broken_cnt

    if att_i == EGG_CNT or broken == EGG_CNT:
        return

    if eggs[att_i][0] <= 0:
        hit(eggs, att_i + 1, broken)

    else:
        for dfn_i in range(EGG_CNT):
            if dfn_i == att_i or eggs[dfn_i][0] <= 0:  # 자기 자신 or 방어 계란 내구도 0이하는 skip
                continue

            # 격파 카운팅
            eggs[att_i][0] -= eggs[dfn_i][1]
            if eggs[att_i][0] <= 0:
                broken += 1

            eggs[dfn_i][0] -= eggs[att_i][1]
            if eggs[dfn_i][0] <= 0:
                broken += 1

            broken_cnt = max(broken_cnt, broken)

            # 다음 격파 계란 이동
            hit(eggs, att_i + 1, broken)

            # 공격 전으로 내구도, broke 초기화. 단, broke 는 공격 후 계란이 깨진 경우에만 초기화
            if eggs[att_i][0] <= 0 < eggs[att_i][0] + eggs[dfn_i][1]:
                broken -= 1
            eggs[att_i][0] += eggs[dfn_i][1]

            if eggs[dfn_i][0] <= 0 < eggs[dfn_i][0] + eggs[att_i][1]:
                broken -= 1
            eggs[dfn_i][0] += eggs[att_i][1]


def solution():
    global EGG_CNT, eggs

    EGG_CNT = int(input().strip())
    eggs = [list(map(int, input().strip().split())) for _ in range(EGG_CNT)]

    hit(eggs, 0, 0)

    print(broken_cnt)


solution()