N = int(input())
arr = [input() for _ in range(N)]
dic = dict()

for word in arr:
    for i in range(1, len(word)+1):
        dic[word[:i]] = dic.get(word[:i], 0) + 1

prefix, p_len = '', 0
for ele, cnt in dic.items():
    l = len(ele)
    if cnt >= 2:
        if l > p_len:
            prefix = ele
            p_len = l


print_cnt = 0
for word in arr:
    if word.startswith(prefix):
        print(word)
        print_cnt += 1
    if print_cnt >= 2:
        break