def my_maze_path():
    import sys
    from collections import deque
    input = sys.stdin.readline
    n, m = map(int, input().split())
    graph = []
    visited = [[False] * m for _ in range(n)]
    # print(visited)

    for _ in range(n):
        graph.append(list(map(int, input().rstrip())))
    # print(graph)

    def bfs(x, y):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        queue = deque([(x, y)])
        # print(queue)

        while queue:
            x, y = queue.popleft()
            visited[x][y] = True
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # print(nx, ny)
                if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1 and visited[nx][ny] is False:
                    # print(nx, ny)
                    queue.append((nx, ny))
                    graph[nx][ny] = graph[x][y] + 1

        return graph[n-1][m-1]

    print(bfs(0, 0))


my_maze_path()