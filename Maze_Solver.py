import random
import os

class MazeSolver:
    def __init__(self, size):
        self.size = size
        self.maze = [['◌'] * size for _ in range(size)]  # Initialize an open space maze
        self.start = (0, 0)
        self.end = (size - 1, size - 1)

    def generate_maze(self, percent_walls):
        num_walls = int((percent_walls / 100) * (self.size ** 2))

        for _ in range(num_walls):
            x, y = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
            self.maze[x][y] = '▓'  # Set ▓ to represent a wall

    def print_maze(self):
        for row in self.maze:
            print(" ".join([self.get_colored_cell(cell) for cell in row]))

    def get_colored_cell(self, cell):
        if cell == '▓':
            return "\033[91m▓\033[0m"  # Red box for walls
        elif cell == '◍':
            return "\033[92m◍\033[0m"  # Green for path
        elif cell == '◌':
            return "\033[94m◌\033[0m"  # Blue for open space
        elif cell == 'S':
            return "\033[93mS\033[0m"  # Yellow for start
        elif cell == 'E':
            return "\033[93mE\033[0m"  # Yellow for end

    def find_path(self):
        visited = set()

        def dfs(x, y):
            if (x, y) == self.end:
                return [(x, y)]

            visited.add((x, y))

            for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if 0 <= nx < self.size and 0 <= ny < self.size and (nx, ny) not in visited and self.maze[nx][ny] == '◌':
                    path = dfs(nx, ny)
                    if path:
                        return [(x, y)] + path

            return []

        path = dfs(*self.start)
        return path

    def print_path(self, path):
        if not path:
            print("\nNo path exists.")
            return

        for row in range(self.size):
            print(" ".join([self.get_colored_path_cell(row, col, path) for col in range(self.size)]))

    def get_colored_path_cell(self, row, col, path):
        cell = self.maze[row][col]
        if (row, col) in path:
            return "\033[92m◍\033[0m"  # Green for path
        else:
            return self.get_colored_cell(cell)
        
    def mark_path_on_maze(self, path):
        for row in range(self.size):
            for col in range(self.size):
                                
                if (row, col) == self.start:
                    self.maze[row][col] = 'S'  # 'S' represents the start point                
                
                elif (row, col) in path:
                    self.maze[row][col] = '◍'  # '◍' represents the path

                if (row, col) == self.end:
                    self.maze[row][col] = 'E'  # 'E' represents the end point        
                
if __name__ == "__main__":
    size = int(input("Enter the size of the maze: "))
    percent_walls = int(input("Enter the percentage of walls (0-100): "))

    maze_solver = MazeSolver(size)
    maze_solver.generate_maze(percent_walls)

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal
        print("\nMaze:")
        maze_solver.print_maze()

        print("\n1. Print the path")
        print("2. Generate another puzzle")
        print("3. Exit the Game")

        user_choice = input("Enter your choice (1/2/3): ")

        if user_choice == "1":
            path = maze_solver.find_path()
            maze_solver.print_path(path)
            if path:
                print("\nPath:")
                maze_solver.mark_path_on_maze(path)
        elif user_choice == "2":
            maze_solver = MazeSolver(size)
            maze_solver.generate_maze(percent_walls)
        elif user_choice == "3":
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
