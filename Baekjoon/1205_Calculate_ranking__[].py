import sys
input = sys.stdin.readline

def solution():
    N, new, P = map(int, input().strip().split())
    
    scores = list(map(int, input().strip().split()))
    scores_len = len(scores)
    scores.append(new)
    
    ranks = [1] * len(scores) # 각 점수 별 등수를 기록
    
    # 일단 내림차순 정렬
    scores.sort(key=lambda x : x * -1)
    
    # 이미 랭킹만큼의 점수가 차있고 태수 점수가 랭킹 꼴찌와 똑같으면 패스
    if scores_len == P and scores[-1] == new:
        sys.stdout.write('-1')
        return
    
    curr_rank = ranks[0]
    for i, score in enumerate(scores):
        if i == 0:
            continue
        
        curr_rank += 1
        if score < scores[i-1]:
            ranks[i] = curr_rank
            
        elif score == scores[i-1]:
            ranks[i] = ranks[i-1]
    
    taesu_rank = ranks[scores.index(new)]
    if taesu_rank <= P:
        sys.stdout.write(f"{taesu_rank}")
    else:
        sys.stdout.write("-1")
        
solution()