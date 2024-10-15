import sys

def solution():
    
    def bt(res, operand, limit, exp):
        if operand > limit:
            return res
        
        # 연산자 '+'
        if bt(res+operand, operand+1, True, limit) == 0:
            exp.append('+') 
        exp.pop()
        
        # 연산자 '-'
        if bt(res-operand, operand+1, False, limit) == 0:
            exp.append('-')
        exp.pop()
        
        
    ans = 0
    
    C = int(sys.stdin.readline().strip())
    for _ in range(C):
        calc = 0
        ans = []
        bt(0, 1, int(sys.stdin.readline().strip()), ans)
            
        
solution()