def get_sequence_index(word: str) -> int:
    """
    주어진 문자열의 길이와 사전순 기준 0-기반 인덱스를 구하는 함수.
    """
    word = word.lower()
    length = len(word)
    index = 0
    
    # Step 1: 현재보다 짧은 문자열들의 총 개수 누적
    for l in range(1, length):
        index += 26 ** l
        
    # Step 2: 현재 길이 내에서 자릿수별 사전순 위치를 26진법으로 계산
    for i, ch in enumerate(word):
        char_val = ord(ch) - ord('a')
        power = length - 1 - i
        index += char_val * (26 ** power)
        
    return index


def get_word_from_index(index: int) -> str:
    """
    주어진 0-기반 순서 인덱스를 정렬 기준(길이 순 -> 사전 순)에 맞는 
    소문자 문자열로 복원하는 함수.
    """
    length = 1
    
    # 1. Step 1: 주어진 인덱스를 통해 문자열의 실제 길이를 결정
    # 길이 1(26^1), 길이 2(26^2) 등의 개수를 차례로 빼며 자릿수를 확정함
    while True:
        count_of_current_length = 26 ** length
        if index < count_of_current_length:
            break
        index -= count_of_current_length
        length += 1
        
    # 2. Step 2: 확정된 길이 내에서 26진법 변환을 통해 알파벳 복원
    result = []
    for i in range(length):
        # 현재 자릿수 뒤로 남은 자릿수 계산 (가중치 결정을 위함)
        power = length - 1 - i
        weight = 26 ** power
        
        # 남은 인덱스를 가중치로 나눈 몫이 해당 자리의 알파벳 인덱스가 됨
        char_val = index // weight
        # 나머지는 다음 자릿수 계산을 위해 넘겨줌
        index %= weight
        
        # 알파벳 정수값(0~25)을 실제 소문자 문자로 변환하여 리스트에 추가
        result.append(chr(ord('a') + char_val))
        
    # 리스트의 문자들을 하나의 문자열로 결합하여 반환
    return "".join(result)


def solution(n: int, bans: list) -> list:
    """
    최초 호출 함수.
    bans 리스트를 정렬한 후, n 이하의 순서를 가진 요소들의 인덱스 리스트를 반환함.
    """
    
    # 1 입력받은 bans 리스트를 [1순위: 길이 오름차순, 2순위: 사전 오름차순]으로 정렬
    # 파이썬의 sort는 기본적으로 문자열을 사전순으로 정렬하므로, key에 len을 주어 길이순을 먼저 적용함
    sorted_bans = sorted(bans, key=lambda x: (len(x), x.lower()))
    
    ans_index = n-1 if n-1 >= 0 else 0 # 갱신할 순서
    
    # 2. 지워진 문자열 개수만큼 찾으려는 순서를 뒤로 이동
    for ban in sorted_bans:
        ban_index = get_sequence_index(ban)
        
        if ban_index <= ans_index: 
            ans_index += 1
    
    # 3. 독립된 정수 n에 해당하는 기준 문자열을 역산으로 구함.
    return get_word_from_index(ans_index)