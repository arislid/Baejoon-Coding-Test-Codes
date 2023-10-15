def solution(triangle):
    answer = 0
    # 어떤 위치(h)의 idx에 대하여 다음으로(h+1) 이동할 수 있는 경우는 idx, idx+1이다.
    # 둘 중 어떤 위치로 가는 게 최고인지 DP에 접근하면서 풀어보자.
    # print(len(triangle))
    h = len(triangle) - 1
    route = [0] * len(triangle)
    route[0] = triangle[0][0]
    
    while h > 0:
        for i in range(h):
            triangle[h-1][i] += max(triangle[h][i], triangle[h][i+1])
        h -= 1
            
    return triangle[0][0]