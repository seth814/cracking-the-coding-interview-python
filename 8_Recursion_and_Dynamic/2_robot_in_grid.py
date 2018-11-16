class Maze:
    
    def __init__(self):
        self.memo = {}
        self.path = []
        self.failed_points = []
    
    def get_path(self, maze):
        if maze == None or len(maze) == 0:
            return None
        if self.is_path(maze, 0, 0):
            return list(reversed(self.path))
        return None
    
    def is_path(self, maze, row, col):
        if row > len(maze)-1 or col > len(maze[0])-1:
            return False
        if maze[row][col] is False:
            return False
        if (row, col) in self.failed_points:
            return False
        
        is_origin = (row == len(maze)-1) and (col == len(maze[0])-1)

        if is_origin or self.is_path(maze, row+1, col) or self.is_path(maze, row, col+1):
            self.path.append((row, col))
            return True
        
        self.failed_points.append((row, col))
        return False
        
    
    def count_paths(self, maze, row, col):
        if row > len(maze)-1 or col > len(maze[0])-1:
            return 0
        if maze[row][col] is False:
            return 0
        if row == len(maze)-1 and col == len(maze[0])-1:
            return 1
        if (row, col) in self.memo.keys():
            return self.memo[(row, col)]
        
        num_paths = self.count_paths(maze, row+1, col) + self.count_paths(maze, row, col+1)
        
        self.memo[(row, col)] = num_paths
        
        return num_paths

maze = [ [True,  True,  True],
         [True,  True,  True],
         [True,  False, True] ]

paths = Maze()
num_paths = paths.count_paths(maze, 0, 0)
path = paths.get_path(maze)

class PacMan:
    
    def max_points(self, grid, n, m):
        if n > len(grid)-1 or m > len(grid[0])-1:
            return 0
        elif (n==len(grid)-1) and (m==len(grid[0])-1):
            return grid[n][m]
        else:
            return grid[n][m] + max(self.max_points(grid,n+1,m), self.max_points(grid,n,m+1))
        
grid = [[0, 1, 21],
        [8, 2, 12],
        [3, 7, 0]]
        
pac = PacMan()
points = pac.max_points(grid, 0, 0)

