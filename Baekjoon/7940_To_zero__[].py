import sys

def solution():
    def BT(res, operand, limit, exp):
        
        if len(exp) >= limit-1:
            if len(exp) == limit - 1 and res == 0:
                sys.stdout.write(f"1")
                for i, op in enumerate(exp):
                    sys.stdout.write(f"{op}{i+2}")
                sys.stdout.write(f"\n")
                return
            else:
                return
        
        if res == 1:
            # 공백, '+'
            exp.append(' ')
            BT(int(f"12"),3, limit, exp)
            exp.pop()
        
        # '+', 공백
        exp.append('+')
        exp.append(' ')
        BT(res+int(f"{str(operand)}"f"{str(operand+1)}"), operand+2, limit, exp)
        exp.pop()
        exp.pop()
        
        # 연산자 '+'
        exp.append('+')
        BT(res+operand, operand+1, limit, exp)
        exp.pop()
        
        # '-', 공백
        exp.append('-')
        exp.append(' ')
        BT(res-int(f"{str(operand)}"f"{str(operand+1)}"), operand+2, limit, exp)
        exp.pop()
        exp.pop()
        
        # 연산자 '-'
        exp.append('-')
        BT(res-operand, operand+1, limit, exp)
        exp.pop()
    
    C = int(sys.stdin.readline().strip())
    for _ in range(C):
        N = int(sys.stdin.readline().strip())
        
        BT(1, 2, N, [])
        sys.stdout.write(f"\n")
        
solution()