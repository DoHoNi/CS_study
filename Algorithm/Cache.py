#https://programmers.co.kr/learn/courses/30/lessons/17680
#2019.08.04


def solution(cacheSize, cities):
    q = []
    time = 0
    if cacheSize ==0 :
        return 5* len(cities)
    for city in cities:
        cur_city = city.lower()
        try:
            cur_index = q.index(cur_city)
        except ValueError:
            cur_index = -1
        
        if cur_index >=0:
            q.pop(cur_index)
            time +=1
        else :
            if len(q) >= cacheSize and cacheSize > 0:
                q.pop(0)
            time += 5
        q.append(cur_city)
    
    return time
