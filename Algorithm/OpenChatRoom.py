#2019.07.23
#https://programmers.co.kr/learn/courses/30/lessons/42888


def solution(record):
    user_dict = {}
    for msg in record:
        cur_msg = msg.split(" ")
        if cur_msg[0] == "Enter" or cur_msg[0] == "Change":
            user_dict[cur_msg[1]] = cur_msg[2]
    
    answer = []
    for msg in record:
        cur_msg = msg.split(" ")
        if cur_msg[0] == "Enter":
            answer.append(user_dict[cur_msg[1]]+"님이 들어왔습니다.")
        if cur_msg[0] == "Leave":
            answer.append(user_dict[cur_msg[1]]+"님이 나갔습니다.")
        
    return answer