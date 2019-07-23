#2019.07.23
#https://programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    cur_level = [0]*(N+2)
    for level in stages:
        cur_level[level] +=1
        
    total_level = [0]*(N+2)
    total_level[N+1] = cur_level[N+1]
    
    fail_rates = [] 
    for i in range(N,0,-1):
        total_level[i] = cur_level[i] + total_level[i+1]
        fail_rate = cur_level[i]/total_level[i] if total_level[i] != 0 else 0
        fail_rates.append((fail_rate,i))
    
    fail_rates.sort(key=lambda k:(k[0],-k[1]) ,reverse=True)
    answer = [ s for rate, s in fail_rates]
    
    return answer