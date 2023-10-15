def soldier_placement():
    import sys
    input = sys.stdin.readline
    n = int(input())
    soldiers = list(map(int, input().split()))
    ans = [1] * (n)

    for i in range(n):
        for j in range(i):
            if soldiers[i] < soldiers[j]:
                ans[i] = max(ans[i], ans[j]+1)

    # print(ans)
    print(len(soldiers) - max(ans))
    
soldier_placement()