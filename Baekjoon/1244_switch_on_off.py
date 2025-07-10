import sys

input = sys.stdin.readline

def solution():
    switch_cnt = int(input())
    switches = list(map(lambda x: True if x == '1' else False, input().split()))
    student_cnt = int(input())
    students = []
    for _ in range(student_cnt):
        students.append(list(map(int, input().split())))

    swap_cnt = [0] * switch_cnt # 각 스위치 별로 눌러야 하는 횟수 기록
    while students:
        sex, num = students.pop(0)

        if sex == 1:
            # 받은 수의 배수
            for i in range(1, switch_cnt//num + 1):
                swap_cnt[(i*num) - 1] += 1
        else:
            # 앞서 쌓인 swap_cnt 적용
            for idx, cnt in enumerate(swap_cnt):
                if cnt % 2 != 0:
                    switches[idx] = not switches[idx]

            swap_cnt = [0] * switch_cnt

            # 좌우 대칭 최대 길이
            curr_idx = num - 1
            offset = 1
            longest_offset = 0
            while offset <= curr_idx:
                if switches[curr_idx-offset] == switches[curr_idx+offset]:
                    longest_offset = offset
                    offset += 1
                else:
                    break
            for j in range(curr_idx-longest_offset, curr_idx+longest_offset+1):
                switches[j] = not switches[j]
            break

    print(switches)

solution()
