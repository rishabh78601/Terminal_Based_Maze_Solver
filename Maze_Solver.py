import random  # Importing the random module for generating random numbers
import os  # Importing the os module for accessing system-specific functions

class MazeSolver:
    def __init__(self, size):
        # Initializing MazeSolver class with the given size
        self.size = size
        self.maze = [['◌'] * size for _ in range(size)]  # Initializing an open space maze
        self.start = (0, 0)
        self.end = (size - 1, size - 1)

    def generate_maze(self, percent_walls):
        # Generating a maze with walls based on the given percentage
        num_walls = int((percent_walls / 100) * (self.size ** 2))

        for _ in range(num_walls):
            x, y = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
            self.maze[x][y] = '▓'  # Setting ▓ to represent a wall

    def print_maze(self):
        # Printing the maze with colored cells
        for row in self.maze:
            print(" ".join([self.get_colored_cell(cell) for cell in row]))

    def get_colored_cell(self, cell):
        # Getting colored representation of a cell based on its content
        if cell == '▓':
            return "\033[91m▓\033[0m"  # Using red box for walls
        elif cell == '◍':
            return "\033[92m◍\033[0m"  # Using green for path
        elif cell == '◌':
            return "\033[94m◌\033[0m"  # Using blue for open space
        elif cell == 'S':
            return "\033[92mS\033[0m"  # Using green for start
        elif cell == 'E':
            return "\033[92mE\033[0m"  # Using green for end

    def find_path(self):
        # Finding a path from the start to the end using depth-first search
        visited = set()

        def dfs(x, y):
            if (x, y) == self.end:
                return [(x, y)]

            visited.add((x, y))

            for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= nx < self.size and 0 <= ny < self.size and (nx, ny) not in visited and self.maze[nx][ny] == '◌':
                    path = dfs(nx, ny)
                    if path:
                        return [(x, y)] + path

            return []

        path = dfs(*self.start)
        return path

    def print_path(self, path):
        # Printing the maze with the discovered path
        if not path:
            print("\nNo path exists.")
            return

        for row in range(self.size):
            print(" ".join([self.get_colored_path_cell(row, col, path) for col in range(self.size)]))

    def get_colored_path_cell(self, row, col, path):
        # Getting colored representation of a cell based on its presence in the path
        cell = self.maze[row][col]
        if (row, col) in path:
            return "\033[92m◍\033[0m"  # Using green for path
        else:
            return self.get_colored_cell(cell)

    def mark_path_on_maze(self, path):
        # Marking the discovered path on the maze
        for row in range(self.size):
            for col in range(self.size):

                if (row, col) == self.start:
                    self.maze[row][col] = 'S'  # 'S' represents the start point

                elif (row, col) in path:
                    self.maze[row][col] = '◍'  # '◍' represents the path

                if (row, col) == self.end:
                    self.maze[row][col] = 'E'  # 'E' represents the end point

if __name__ == "__main__":
    # Getting input from the user to initialize and interact with the MazeSolver
    size = int(input("Entering the size of the maze: "))
    percent_walls = int(input("Entering the percentage of walls (0-100): "))

    maze_solver = MazeSolver(size)
    maze_solver.generate_maze(percent_walls)

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clearing the terminal
        print("\nMaze:")
        maze_solver.print_maze()

        # Presenting options to the user
        print("\n1. Printing the path")
        print("2. Generating another puzzle")
        print("3. Exiting the Game")

        user_choice = input("Entering your choice (1/2/3): ")

        # Acting based on user's choice
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
