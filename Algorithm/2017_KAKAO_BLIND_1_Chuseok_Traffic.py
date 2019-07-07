# 2017_KAKAO_BLIND_RECRUTMENT_1차
# 추석트레픽

# https://programmers.co.kr/learn/courses/30/lessons/17676
# 2019.07.07 
# Dohyun Kim

def get_sec(time):
    sec = 0
    for i , t in enumerate(time.split(':')) :
        sec += float(t) * (60 ** (2-i))
    return sec 

def preprocessing(lines):
    s_r_list = []
    for line in lines :
        split_data = line.split()
        response_time = get_sec(split_data[1])
        start_time = response_time - float(split_data[2][:-1]) + 0.001
        s_r_list.append((start_time, response_time))
    return s_r_list

def solution(lines):
    cur_time = 0
    max_ = 0
    s_r_list = preprocessing(lines)
    len_list = len(s_r_list)
    for i , s_r in enumerate(s_r_list):
        cur_start_time = s_r[1]
        cur_end_time = s_r[1] + 1
        cnt = 0
        for j in range(i,len_list):
            if s_r_list[j][0] >= cur_end_time or s_r_list[j][1] < cur_start_time :
                continue
            else :
                #print("cnt", cnt)
                cnt = cnt+1
        if cnt > max_ :
            max_ = cnt
    return max_