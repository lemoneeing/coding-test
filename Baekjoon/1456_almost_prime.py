import sys


min, mx = map(int, sys.stdin.readline().split())
a = [i for i in range(0, 1000001)]
a[1] = 0
cnt = 0

# mx_root = int(mx**(1/2))
# for i in range(2, mx_root+1):
#     if a[i] == 0:
#         continue
#
#     for j in range(i+i, mx+1, i):
#         a[j] = 0

# for num in a[int(min**(1/2)):mx+1]:
#     if num == 0:
#         continue
#
#     tmp = num
#     while (min / tmp) <= num <= (mx / tmp):
#         cnt += 1
#         tmp *= num

for i in range(2, int(1000001**(1/2))+1):
    if a[i] == 0:
        continue

    for j in range(i+i, 1000001, i):
        a[j] = 0

for num in a[2:]:
    if num == 0:
        continue

    tmp = num
    while (float(min) / float(tmp)) <= float(num) <= (float(mx) / float(tmp)):
        cnt += 1
        tmp *= num

sys.stdout.write(f"{cnt}")