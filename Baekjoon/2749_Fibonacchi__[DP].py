import sys
input = sys.stdin.readline

def solution():
    N = int(input().strip())
    
    
    # 보통의 일반적인 피보나치 + 메모리 초과를 피하기 위해 배열 3칸만 이용. -> 시간 초과
    # fib = [0, 1] 
    # for i in range(2, N+1):
    #     fib.append(fib[0] + fib[1])
    #     fib = fib[1:]
        
    # sys.stdout.write(f"{fib[-1] % 1000000}")
    
    
    # 피사노 주기(https://www.acmicpc.net/problem/9471) 를 이용한 피보나치 나머지 구하기
    fib_with_fisano = [0] * 1500001
    fib_with_fisano[0] = 0
    fib_with_fisano[1] = 1
    for i in range(2, 1500001):
        fib_with_fisano[i] = (fib_with_fisano[i-1] + fib_with_fisano[i-2]) % 1000000
        
    sys.stdout.write(f"{fib_with_fisano[N%1500000]}")
    
solution()