class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        q = [e+1 for e in range(n)]
        while len(q) > 1:
            target = k % len(q) - 1
            if target >= 0:
                q = q[target+1:] + q[:target]
            else:
                q = q[:target]
            
        return q[0]
            
    
if __name__ == "__main__":
    print(Solution().findTheWinner(5, 2))
    print(Solution().findTheWinner(6, 5))
    print(Solution().findTheWinner(5, 4))