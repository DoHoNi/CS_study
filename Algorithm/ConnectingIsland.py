def find(parents_list, n):
    if n == parents_list[n]:
        return n 
    return find(parents_list, parents_list[n])

def solution(n,costs):
    if n == 1 : 
        return 0
    link = 0
    cur_cost = 0
    costs.sort(key=lambda tup:tup[2])
    parents_list = list(range(n))
    for cost in costs :
        if link >= n-1:
            break
        first = find(parents_list, cost[0])
        second = find(parents_list, cost[1])
        if first == second :
            continue
        else : 
            parents_list[second] = first
            link = link +1
            cur_cost = cur_cost + cost[2]
            
    return cur_cost

'''
def solution(n, costs):
    if n == 1:
        return 0
    link = 0
    answer = 0
    isvisit = [-1]*n
    costs.sort(key=lambda tup:tup[2])
    for cost in costs:
        #print(link, cost,isvisit)
        if link >= n-1:
            break
        g_num1, g_num2 = isvisit[cost[0]], isvisit[cost[1]]
        if g_num1 >0 and g_num1 == g_num2:
            continue
        link +=1
        answer +=cost[2]
        if g_num1 <0 and g_num2<0 : 
            isvisit[cost[0]] = link
            isvisit[cost[1]] = link
            continue
            
        new_num = max(g_num1,g_num2)
        pre_num = min(g_num1,g_num2)
        if pre_num <0 :
            target = cost[0] if isvisit[cost[0]] < isvisit[cost[1]] else cost[1]
            isvisit[target] = new_num
        else :
            for i in range(n):
                if isvisit[i] == pre_num:
                    isvisit[i] = new_num
        
    return answer
'''
