import sys


expr_minus_group = sys.stdin.readline().split('-')
answer = 0

for i, group in enumerate(expr_minus_group):
    group_sum = 0
    for num in group.split('+'):
        group_sum += int(num)

    if i == 0:
        answer += group_sum
    else:
        answer -= group_sum

sys.stdout.write(f"{answer}")


