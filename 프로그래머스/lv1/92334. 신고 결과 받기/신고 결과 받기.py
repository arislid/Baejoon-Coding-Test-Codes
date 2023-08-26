def solution(id_list, report, k):
    answer = [0 for i in range(len(id_list))]
    
    id_dict = {k:[] for k in id_list}
    r_id_dict = {k:0 for k in id_list}
    _report = list(set(report))
    # print(_report)
    # print(r_id_dict)
    stop_id = []
    for i in range(len(_report)):
        user_id, report_id = _report[i].split(' ')
        # print(user_id, report_id)
        id_dict[user_id].append(report_id)
        r_id_dict[report_id] += 1
        if r_id_dict[report_id] >= k and report_id not in stop_id:
            stop_id.append(report_id)
    
    # print(f"stop_id: {stop_id}")
    # print(f"id_dict: {id_dict}")
    # print(f"r_id_dict: {r_id_dict}")
    
    for i, user in enumerate(id_dict):
        # print(i, id_dict[user])
        for j in range(len(id_dict[user])):
            if id_dict[user][j] in stop_id:
                answer[i] += 1
                
    
    
    
    
    
    
    return answer