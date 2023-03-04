def solution(t, p):
    answer = 0
    t_list = list(t)
    sub_t = ''
    for i in range(len(t_list) - len(p) + 1):
        for j in range(len(p)):
            sub_t += t_list[i+j]
        if int(sub_t) <= int(p):
            answer += 1
        sub_t = ''
            
    return answer