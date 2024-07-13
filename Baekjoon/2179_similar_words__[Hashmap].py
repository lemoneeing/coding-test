import sys

# 동호식 풀이: 난 실패
def solution():
    N = int(sys.stdin.readline())
    words = []
    srt_words = []

    for _ in range(N):
        word = sys.stdin.readline().strip()
        words.append(word)
        srt_words.append([_] + [ord(ch) for ch in word])
    
    # 문자열을 사전순으로 정렬, 각 요소의 0번째는 각 단어의 원래 위치    
    srt_words.sort(key=lambda x: x[1:])

    p = 0
    best_pair_idx = []
    mx_overlap = ''
    for c in range(1, N):
        overlap = ''
        prv = words[srt_words[p][0]]
        curr = words[srt_words[c][0]]
        
        # 최대 비슷 보다 문자열 길이가 짧으면 스킵
        if len(mx_overlap) > len(prv) or len(mx_overlap) > len(curr):
            continue
        
        # 비교할 문자열들이 아예 같으면 원래 위치가 더 앞쪽인 인덱스 기억
        if prv == curr:
            p = min(srt_words[p][0], srt_words[c][0])
            continue
        
        # 앞 문자열과 비교
        shorter, longer = (prv, curr) if len(prv) < len(curr) else (curr, prv)
        for i, ch in enumerate(shorter):
            if ch == longer[i]:
                overlap += ch
        
        curr_pair_idx = [srt_words[p][0], srt_words[c][0]]  # 문자열의 원래 위치를 저장
        # 더 긴 비슷을 찾았을 때
        if len(mx_overlap) < len(overlap):
            mx_overlap = overlap
            best_pair_idx = curr_pair_idx
        
        # 길이가 같은 비슷을 찾았을 때
        elif len(overlap) > 0 and len(mx_overlap) == len(overlap):
            # 비슷이 아예 같으면 가장 작은 인덱스 두 개 고르기
            if mx_overlap == overlap:
                best_pair_idx = sorted(set(best_pair_idx + curr_pair_idx))[:2]
            else:
                # 가장 작은 요소가 있는 페어 선택
                best_pair_idx.sort()
                curr_pair_idx.sort()
                if best_pair_idx[0] > curr_pair_idx[0]:
                    best_pair_idx = curr_pair_idx
                elif best_pair_idx[0] == curr_pair_idx[0] and best_pair_idx[1] > curr_pair_idx[1]:
                    best_pair_idx = curr_pair_idx
        
        p = c

    best_pair_idx.sort()
    for i in best_pair_idx:
        sys.stdout.write(f"{words[i]}\n")
      
      
# 현도식 풀이
def solution():
    N = int(sys.stdin.readline())
    words = []
    prefixes = {}
    
    for _ in range(N):
        word = sys.stdin.readline().strip()
        words.append(word)
        for i in range(1, len(word)+1):
            prefixes[word[:i]] = prefixes.get(word[:i], 0) + 1
    
    mx_len = 0
    best = ''   # 가장 긴 접두사
    for k, v in prefixes.items():
        if v > 1:
            # 접두사가 가장 긴 것으로 갱신
            if mx_len < len(k):
                mx_len = len(k)
                best = k
       
    print_cnt = 0  
    for w in words:
        if w.startswith(best):
            sys.stdout.write(f"{w}\n")
            print_cnt+=1
            
            if print_cnt == 2:
                break

solution()