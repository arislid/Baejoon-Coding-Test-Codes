def solution(wallpaper):
    lux, luy, rdx, rdy = 0, 0, 0, 0
    x = []
    y = []
    # for i in wallpaper:
    #     print(i)
    # print()
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                x.append(i)
                y.append(j)
    
#     print(min(x), min(y))
#     print(max(x), max(y))
    
    answer = [min(x), min(y), max(x)+1, max(y)+1]
    # print(len(wallpaper), len(wallpaper[0]))
    return answer