import sys

def solution():
    def BT(res, operand, limit, exp):
        
        if len(exp) == limit:
            if res == 0:
                sys.stdout.write(f"1")
                for i, op in enumerate(exp[1:]):
                    sys.stdout.write(f"{op}{i+2}")
                sys.stdout.write(f"\n")
                return
            else:
                return

        if len(exp) > 0:
            # 공백
            exp.append(' ')
            BT(res, operand*10+operand+1, limit, exp)
            exp.pop()
        
        # 연산자 '+'
        exp.append('+')
        BT(res+operand, operand+1, limit, exp)
        exp.pop()
        
        if len(exp) > 0:
            # 연산자 '-'
            exp.append('-')
            BT(res-operand, operand+1, limit, exp)
            exp.pop()
    
    C = int(sys.stdin.readline().strip())
    for _ in range(C):        
        BT(0, 1, int(sys.stdin.readline().strip()), [])
        sys.stdout.write(f"\n")
        
solution()