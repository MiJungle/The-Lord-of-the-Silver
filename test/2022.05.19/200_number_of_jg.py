class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(graph, start):
            q = deque()
            x, y = start
            visited[x][y] = True
            q.append(start)
            
            while q:
                x,y = q.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny] or graph[nx][ny] == "0":
                        continue
                    visited[nx][ny] = True
                    q.append((nx,ny))
        m = len(grid[0])
        n = len(grid)
        visited = [[False for _ in range(m)] for _ in range(n)]
        dx = [-1, 1, 0, 0]
        dy = [0, 0, 1, -1]
        result = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and not visited[i][j]:
                    bfs(grid, (i, j)) 
                    result +=1
                # print(visited)
        return(result)
            
                
