import sys

min, mx = map(int, sys.stdin.readline().split())
a = [i for i in range(0, mx+1)]
a[1] = 0

mx_root = int(mx**(1/2))
for i in range(2, mx_root+1):
    if a[i] == 0:
        continue

    for j in range(i*2, mx+1, i):
        a[j] = 0


for num in a[min:]:
    if num != 0:
        sys.stdout.write(f"{num}\n")