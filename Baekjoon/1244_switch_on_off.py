import sys
input = sys.stdin.readline

def solution(switch_cnt, switches, student_cnt, students):
# def solution():
#     switch_cnt = int(input())
#     switches = list(map(int, input().split()))
#
#     student_cnt = int(input())
#     students = []
#     for _ in range(student_cnt):
#         students.append(list(map(int, input().split())))

    swap_cnt = [0] * switch_cnt  # 각 스위치 별로 눌러야 하는 횟수 기록
    while students:
        b_or_g, num = students.pop(0)

        # 받은 수의 배수
        if b_or_g == 1:
            for i in range(1, switch_cnt//num + 1):
                swap_cnt[(i*num) - 1] += 1

        else:
            if sum(swap_cnt) > 0:  # 앞서 쌓인 swap_cnt 적용
                for idx, cnt in enumerate(swap_cnt):
                    if cnt % 2 != 0:
                        switches[idx] = (switches[idx] + 1) % 2

            swap_cnt = [0] * switch_cnt     # 각 스위치 별로 눌러야 하는 횟수 기록

            # 좌우 대칭 최대 길이
            curr_idx = num - 1
            offset = 1
            longest_offset = 0
            while 0 <= curr_idx-offset and curr_idx+offset <= switch_cnt - 1:
                if switches[curr_idx-offset] == switches[curr_idx+offset]:
                    longest_offset = offset
                    offset += 1
                else:
                    break
            for j in range(curr_idx-longest_offset, curr_idx+longest_offset+1):
                switches[j] = (switches[j] + 1) % 2

    if sum(swap_cnt) > 0:  # 앞서 쌓인 swap_cnt 적용
        for idx, cnt in enumerate(swap_cnt):
            if cnt % 2 != 0:
                switches[idx] = (switches[idx] + 1) % 2

    idx_in_a_line = 0
    for on_off in switches:
        sys.stdout.write(f"{on_off} ")

        if idx_in_a_line >= 19:
            idx_in_a_line = 0
            sys.stdout.write(f"\n")
            continue

        idx_in_a_line += 1

# solution(45, [1 for _ in range(45)], 1, [(1, 3)])
# solution(10, list(map(int, '0 1 0 0 1 1 0 0 0 0'.split())), 2, [(2, 3), (2, 4)])
solution(10, list(map(int, '0 1 0 0 1 1 1 1 1 1'.split())), 2, [(2, 2)])
