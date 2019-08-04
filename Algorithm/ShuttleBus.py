#https://programmers.co.kr/learn/courses/30/lessons/17678
#2019.08.04


def my_shuttle(cur_time, shuttles, m):
    for i in range(len(shuttles)):
        if cur_time <= shuttles[i][0] and shuttles[i][2] < m:
            return i
    return -1

def str_time(time):
    str_h = "0"+str(int(time/60)) if int(time/60) <10 else str(int(time/60))
    str_m = "0"+ str(int(time%60)) if time%60 <10 else  str(int(time%60))
    return str_h+":"+str_m

def solution(n, t, m, timetable):
    shuttles = []
    start = 9*60 #9:00
    for i in range(n):
        shuttles.append([start+(t*i),0,0])
    
    timetable.sort()
    for time in timetable:
        tmp = time.split(":")
        cur_time = int(tmp[0])*60 + int(tmp[1])
        s_num = my_shuttle(cur_time, shuttles, m)
        if s_num <0 :
            break
        shuttles[s_num]= [shuttles[s_num][0], max(shuttles[s_num][1], cur_time), shuttles[s_num][2]+1]
    
    if shuttles[-1][2] < m:
        shuttles[-1][1] = max(shuttles[-1][0], shuttles[-1][1])
        return str_time(shuttles[-1][1])
    else :
        if shuttles[-1][1] == 0 :
            shuttles[-1][1] = shuttles[-1][0]
        return str_time(shuttles[-1][1]-1)
    
    return answer
