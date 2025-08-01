import sys

input = sys.stdin.readline


def solution():
    class_cnt = int(input())
    students = list(map(int, input().split()))
    main, sub = map(int, input().split())

    ans = 0
    for i in range(class_cnt):
        needs = 1
        if students[i] - main > 0:
            need_sub = (students[i] - main) % sub
            needs += (students[i] - main) / sub if need_sub == 0 else (students[i] - main) // sub + 1

        ans += needs

    sys.stdout.write(f"{int(ans)}")

solution()
