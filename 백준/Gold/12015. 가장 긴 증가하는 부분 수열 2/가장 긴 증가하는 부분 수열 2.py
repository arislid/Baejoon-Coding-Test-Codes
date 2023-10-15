def longest_increment_binary():
    import sys
    n = int(sys.stdin.readline())
    an = list(map(int, sys.stdin.readline().split()))
    series = [an[0]]

    for i in range(n):
        if series[-1] < an[i]:
            series.append(an[i])
        else:
            start = 0
            end = len(series)-1
            while start < end:
                mid = (start + end) // 2
                if series[mid] < an[i]:
                    start = mid + 1
                else:
                    end = mid
            series[end] = an[i]

    # print(series)
    print(len(series))
    
longest_increment_binary()