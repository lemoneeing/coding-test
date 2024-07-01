import sys

cnt = int(sys.stdin.readline())
meetings = [tuple(map(int, sys.stdin.readline().split())) for i in range(cnt)]
meetings.sort(key=lambda x: (x[1], x[0]))
avail_cnt = 0
curr_time = 0

for meeting in meetings:
    if meeting[0] >= curr_time:
        avail_cnt += 1
        curr_time = meeting[1]

sys.stdout.write(f"{avail_cnt}")