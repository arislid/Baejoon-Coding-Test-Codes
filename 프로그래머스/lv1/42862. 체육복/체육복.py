def solution(n, lost, reserve):
    answer = 0
    rent_count = 0
    total = set(lost) | set(reserve) # [2, 3], [3, 4] = [2, 3, 4]
    common = set(lost) & set(reserve) # [2, 3], [3, 4] = [3]
    real_reserve = set(reserve) - set(lost)
    real_lost = set(lost) - set(reserve) # [2]
    check = total - common # [2, 4]
    
    if len(real_lost) == n:
        return 0
    elif len(real_lost) == 0:
        return n
    else:
        for i in check:
            if i in real_lost:
                if i-1 in real_reserve:
                    rent_count += 1
                    real_reserve.remove(i-1)
                elif i+1 in real_reserve:
                    rent_count += 1
                    real_reserve.remove(i+1)
        return n - (len(lost) - rent_count) + len(common)