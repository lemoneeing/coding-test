from datetime import datetime
def solution(m, musicinfos):
    answer = ''

    # 방금그곡 서비스에서는 음악 제목, 재생이 시작되고 끝난 시각, 악보를 제공한다.
    # 네오가 기억한 멜로디와 악보에 사용되는 음은 C, C#, D, D#, E, F, F#, G, G#, A, A#, B 12개이다.
    # 각 음은 1분에 1개씩 재생된다. 음악은 반드시 처음부터 재생되며 음악 길이보다 재생된 시간이 길 때는 음악이 끊김 없이 처음부터 반복해서 재생된다. 음악 길이보다 재생된 시간이 짧을 때는 처음부터 재생 시간만큼만 재생된다.
    # 음악이 00:00를 넘겨서까지 재생되는 일은 없다.
    # 조건이 일치하는 음악이 여러 개일 때에는 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환한다. 재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환한다.
    # 조건이 일치하는 음악이 없을 때에는 “(None)”을 반환한다.

    target_melody = m.replace("C#", 'H')
    longest_played_time = 0
    curr_best_music = "(None)"
    for info_str in musicinfos:
        m_info = info_str.split(',')
        m_title = m_info[2]
        m_info[3] = m_info[3].replace("C#", "H")
        m_len = len(m_info[3])

        # 재생 시간을 초 단위로 계싼
        play_time = int((datetime.strptime(m_info[1], "%M:%S") - datetime.strptime(m_info[0], "%M:%S"))
                        .total_seconds())


        # 실제 재생된 멜로디
        played_melody = ''
        if play_time < m_len:
            played_melody = m_info[3][:play_time]
        elif play_time == m_len:
            played_melody = m_info[3]
        else:
            played_melody = m_info[3] * (play_time // m_len)
            if play_time % m_len > 0:
                played_melody += m_info[3][:play_time % m_len]
        
        if target_melody in played_melody:
            if longest_played_time < play_time:
                longest_played_time = play_time
                curr_best_music = m_title

    return curr_best_music

# print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
# print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))