class Solution:
    def partitionString(self, s: str) -> int:
        curr = ''
        i = 1
        for ch in s:
            # 중복 문자가 나올 때까지 curr 에 ch 추가
            if ch not in curr:
                curr += ch
            # 중복 문자 차례일 때 curr 을 ch 로 초기화, i 는 1 증가
            else:
                i += 1
                curr = ch
        
        return i
        
        
print(Solution().partitionString("abacaba"))