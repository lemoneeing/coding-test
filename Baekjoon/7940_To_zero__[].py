import sys

def solution():
    
    def bt(res, operand, limit, exp):
        if operand > limit:
            return res
        
        # 연산자 '+'
        if bt(res+operand, operand+1, True, limit) == 0:
            exp.append('+') 
        
        # 연산자 '-'
        if bt(res-operand, operand+1, False, limit) == 0:
            exp.append('-')
        
        
    ans = 0
    
    C = int(sys.stdin.readline().strip())
    for _ in range(C):
        calc = 0
        ans = []
        N = int(sys.stdin.readline().strip())
        bt(0, 1, N, ans)
        
        sys.stdout.write(f"1")
        for i in range(2, N+1):
            sys.stdout.write(f"{ans.pop()}{i}")
        
solution()