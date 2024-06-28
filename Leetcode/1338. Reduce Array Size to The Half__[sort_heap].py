from queue import PriorityQueue
from typing import List

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        # cnt = PriorityQueue()
        # cal = {}
        # for n in arr:
        #     if n in cal and cal[n]:
        #         continue

        #     cnt.put((arr.count(n) * -1, n))
        #     cal[n] = True

        # ans = []
        # tLen = len(arr) // 2
        # while len(arr) > tLen:
        #     curr = cnt.get()
        #     while curr[1] in arr:
        #         arr.remove(curr[1])

        #     ans.append(curr[1])

        # return len(ans)
        
        # pq = PriorityQueue()
        
        # cnt = set(arr)
        # for n in cnt:
        #     pq.put((arr.count(n) * -1, n))
        
        cnt = {}
        for n in arr:
            if n in cnt:
                cnt[n] += 1
            else:
                cnt[n] = 1
                
        # for frq in cnt.values():
        #     pq.put(frq)
        
        # sub_len = 0
        # ans = 0
        # targL = len(arr)//2
        # while sub_len < targL:
        #     sub_len += (pq.get()[0] * -1)
        #     ans += 1
            
        # return ans
    
    
        pq = dict(sorted(cnt.items(), key=lambda v: v[1], reverse=True))
        
        ans = 0
        subL = 0
        tgtL = len(arr)//2
        for n, f in pq.items():
            if subL >= tgtL:
                return ans
            ans += 1
            subL += f
    
print(Solution().minSetSize([3,3,3,3,5,5,5,2,2,7]))
print(Solution().minSetSize([9,77,63,22,92,9,14,54,8,38,18,19,38,68,58,19]))