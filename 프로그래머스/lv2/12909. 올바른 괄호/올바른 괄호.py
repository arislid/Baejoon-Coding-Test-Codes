def solution(s):
    answer = True
    
    open_cnt = 0
    cls_cnt = 0
    
    for x in s:
        if x == '(':
            open_cnt += 1
        else:
            cls_cnt += 1
        
        if open_cnt < cls_cnt:
            answer = False
    
    if open_cnt != cls_cnt:
        answer = False
    return answer