import sys

def solution():
    def BT(res, order, limit, exp, nums):
        
        if order > limit:
            if res == 0:
                sys.stdout.write(f"1")
                for i in range(1, limit):
                    sys.stdout.write(f"{exp[i-1]}{nums[i]}")
                sys.stdout.write(f"\n")
                return
            else:
                return
        
        if order == 2:
            exp.append(' ')
            nums.append(order)
            BT(12, 3, limit, exp, nums)
            exp.pop()
            nums.pop()
        
        # '+', 공백
        if order <= limit -1:
            exp.append('+')
            exp.append(' ')
            nums.append(order)
            nums.append(order+1)
            BT(res+int(f"{str(order)}"f"{str(order+1)}"), order+2, limit, exp, nums)
            exp.pop()
            exp.pop()
            nums.pop()
            nums.pop()
        
        # 연산자 '+'
        exp.append('+')
        nums.append(order)
        BT(res+order, order+1, limit, exp, nums)
        exp.pop()
        nums.pop()
        
        # '-', 공백
        if order <= limit -1:
            exp.append('-')
            exp.append(' ')
            nums.append(order)
            nums.append(order+1)
            BT(res-int(f"{str(order)}"f"{str(order+1)}"), order+2, limit, exp, nums)
            exp.pop()
            exp.pop()
            nums.pop()
            nums.pop()
        
        # 연산자 '-'
        exp.append('-')
        nums.append(order)
        BT(res-order, order+1, limit, exp, nums)
        exp.pop()
        nums.pop()
    
    C = int(sys.stdin.readline().strip())
    for _ in range(C):
        N = int(sys.stdin.readline().strip())
        
        BT(1, 2, N, [], [1])
        sys.stdout.write(f"\n")
        
solution()