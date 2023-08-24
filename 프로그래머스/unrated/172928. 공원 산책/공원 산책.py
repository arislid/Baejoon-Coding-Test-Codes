def solution(park, routes):
    answer = []
    matrix = [[p[i] for i in range(len(p))] for p in park]
    start_x = 0
    start_y = 0
    for y, line in enumerate(park):
        for x, l in enumerate(line):
            if l == "S":
                start_x = x
                start_y = y
                break
    # print(start_x, start_y)
    # matrix[y][x]
    x, y = start_x, start_y
    # print(f"start point: {start_y}, {start_x}")
    for route in routes:
        dx, dy = 0, 0
        directions = route.split()
        # directions[0] = 'E'
        # directions[1] = '2'
        if directions[0] == 'E':
            dx += int(directions[1])
            if 0 <= x + dx < len(matrix[0]):
                row = matrix[y][x+1:x+dx+1]
                # print("row: ", row)
                if "X" not in row:
                    x += dx
        elif directions[0] == 'W':
            dx -= int(directions[1])
            if 0 <= x + dx < len(matrix[0]):
                row = matrix[y][x+dx: x]
                # print("row: ", row)
                if "X" not in row:
                    x += dx
        elif directions[0] == 'S':
            dy += int(directions[1])
            if 0 <= y + dy < len(matrix):
                column = [matrix[i][x] for i in range(y+1, y+dy+1)]
                # print("column: ", column)
                if "X" not in column:
                    y += dy
        elif directions[0] == 'N':
            dy -= int(directions[1])
            if 0 <= y + dy < len(matrix):
                column = [matrix[i][x] for i in range(y+dy, y)]
                # print("column: ", column)
                if "X" not in column:
                    y += dy
        
        # print(f"y, x: {y}, {x}")
    answer = [y, x]
    return answer