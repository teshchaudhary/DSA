from collections import deque

def shortest_path_in_maze(maze, start, end):

    n, m = len(maze), len(maze[0])
    sr, sc = start
    er, ec = end

    if maze[sr][sc] == 0 or maze[er][ec] == 0:
        return -1  # blocked start or end

    # Directions: up, down, left, right
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    visited = [[False]*m for _ in range(n)]
    queue = deque([(sr, sc, 0)])  # (row, col, distance)
    visited[sr][sc] = True

    while queue:
        x, y, dist = queue.popleft()

        if (x, y) == (er, ec):
            return dist

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < n and 0 <= new_y < m:
                if not visited[new_x][new_y] and maze[new_x][new_y] == 1:
                    visited[new_x][new_y] = True
                    queue.append((new_x, new_y, dist + 1))

    return -1  # no path found
