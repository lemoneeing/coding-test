class Solution:
    def frequencySort(self, s: str) -> str:
        
        # 빈도수와 일치하는 index 순서에 각 문자 추가
        frq = [[] for _ in range((len(s) + 1))]
        for ch in set(s):
            i = s.count(ch)
            frq[i].append(ch)
        
        # 역순으로 문자열을 인덱스 크기만큼 반복하여 집어넣기
        ans = []
        for j in range(len(frq)-1, 0, -1):
            for e in frq[j]:
                ans.extend([e]*j)
            
        return ''.join(ans)
    
    
if __name__ == "__main__":
    print(Solution().frequencySort("tree"))