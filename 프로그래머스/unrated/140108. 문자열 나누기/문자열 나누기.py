def solution(s):
    answer = ''
    ans = []
    for idx, letter in enumerate(s):
        if len(answer) == 0:
            first = s[idx]
            answer = first
            if idx == len(s) - 1:
                ans.append(answer)
            
        else:
            answer += letter
            if int(len(answer) // 2) == answer.count(first):
                ans.append(answer)
                answer = ''
            elif idx == len(s) - 1:
                ans.append(answer)

    return len(ans)
