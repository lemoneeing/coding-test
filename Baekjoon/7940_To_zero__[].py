import sys

def solution():
    
    # # 문제 잘못 이해: 1 ~ N 까지만 사용하는 줄
    # def BT(res, operand, limit, exp):
        
    #     if operand > limit:
    #         if res == 0:
    #             sys.stdout.write(f"1")
    #             for i, op in enumerate(exp):
    #                 sys.stdout.write(f"{op}{i+2}")
    #             sys.stdout.write(f"\n")
    #             return
    #         else:
    #             return
        
    #     # 연산자 '+'
    #     exp.append('+')
    #     BT(res+operand, operand+1, limit, exp)
    #     exp.pop()
        
    #     # 연산자 '-'
    #     exp.append('-')
    #     BT(res-operand, operand+1, limit, exp)
    #     exp.pop()
        
    
    # C = int(sys.stdin.readline().strip())
    # for _ in range(C):
    #     N = int(sys.stdin.readline().strip())
    #     BT(1, 2, N, [])
    #     sys.stdout.write(f"\n")
solution()