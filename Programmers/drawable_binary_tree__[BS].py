# 처음 생각한 풀이 -> 루트 노드가 되는 숫자는 0이면 안된다고 오판
        
# def check_tree(sub_tree):
#
#     mid = (len(sub_tree))//2
#     left_t = sub_tree[:mid]
#     right_t = sub_tree[mid+1:]
#
#     # mid 번째 노드가 0이면 자식노드도 0이어야 함. = 더미의 자식도 더미여야 함.
#     if sub_tree[mid] == '0':
#         if sub_tree[mid-1] != '0' or sub_tree[mid+1] != '0': # 왜 틀리지?
#             return 0
#
#     if mid >= 3:
#         if check_tree(left_t) and check_tree(right_t):
#             return 1
#         else:
#             return 0
#     else:
#         return 1

def check_tree(tree):
    mid = (len(tree)-1)//2
    left_t = tree[:mid]
    right_t = tree[mid+1:]

    if tree[mid] == '0' and (left_t[mid//2] != '0' or right_t[mid//2] != '0'):
        return 0

    if mid >= 3:
        if check_tree(left_t) == 0 or check_tree(right_t) == 0:
            return 0
        else:
            return 1
    else:
        return 1
    
def solution(numbers):
    answer = []
    
    for n in numbers:
        # 이진수 길이가 포화 이진트리를 구성할 수 있을 만큼(2**n-1) 왼쪽에 0 추가
        bin_num = str(bin(n))[2:]
        pow_limit = 2
        while len(bin_num) >= pow_limit: 
            pow_limit *= 2
        
        bin_num = ('0' * (pow_limit - 1 - len(bin_num))) + bin_num
        
        answer.append(check_tree(bin_num))
        
    return answer

print(solution([5, 2232, 63, 111, 95, 129, 128, 16, 15, 14, 13])) #0 1 1 1 0 0 1 0 1 1 0
# print(solution([95]))

