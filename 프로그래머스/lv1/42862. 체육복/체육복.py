def solution(n, lost, reserve):
    answer = 0
    
    students = [1] * (n+1)
    for i in lost:
        students[i] = 0
    for i in reserve:
        if i in lost:
            students[i] = 1
        else:
            students[i] = 2
    # print(students)
    
    for idx, stu in enumerate(students):
        if idx == 0:
            continue
        elif idx < n and students[idx] == 2:
            if students[idx-1] == 0:
                students[idx-1] += 1
                students[idx] -= 1
            elif students[idx+1] == 0:
                students[idx+1] += 1
                students[idx] -= 1
        elif idx == n:
            if students[idx] == 0 and students[idx-1] == 2:
                studnets[idx] += 1
                students[idx-1] -= 1
            elif students[idx] == 2 and students[idx-1] == 0:
                students[idx] -= 1
                students[idx-1] += 1
    # print(students)
    # print(students.count(1))
    # print(students.count(2))
    answer = students.count(2) + students.count(1) - 1
    return answer