class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        num_islands = 0
        directions = [(0,1), (0,-1), (1,0), (-1,0)]  # Right, Left, Down, Up

        def bfs(r, c):
            queue = deque([(r, c)])
            grid[r][c] = '0'  # Mark as visited
            
            while queue:
                x, y = queue.popleft()
                
                for dx, dy in directions:
                    new_x, new_y = x + dx, y + dy
                    
                    # Check within bounds and if it's land
                    if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x][new_y] == '1':
                        queue.append((new_x, new_y))
                        grid[new_x][new_y] = '0'  # Mark as visited
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':  # Found a new island
                    num_islands += 1
                    bfs(r, c)  # Perform BFS to mark all connected land
        
        return num_islands