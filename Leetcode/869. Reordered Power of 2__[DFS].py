from copy import deepcopy


class Solution:
    nArr = []
    used = []
    
    def reorderedPowerOf2(self, n: int) -> bool:
        self.nArr = list(map(int, str(n)))
        self.used = [False for _ in self.nArr]
        
        for i, n in enumerate(self.nArr):
            if n%2==0:
                self.used[i] = True
                if self.dfs([n]):
                    return True
        
        return False

    def dfs(self, cmb):
        if len(cmb) == len(self.nArr):
            num = int(''.join(cmb))
            if num&(num-1) == 0:
                return True
            else:
                return False
        
        for j, n in enumerate(self.nArr):
            if self.used[j]:
                continue
            cmb.insert(0, n)
            return self.dfs(cmb)
            

if __name__ == "__main__":
    print(Solution().reorderedPowerOf2("42104"))
        
        
        