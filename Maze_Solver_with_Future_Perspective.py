import random
import os
import heapq
from queue import Queue

class MazeSolver:
    def __init__(self, size):
        self.size = size
        self.maze = [['◌'] * size for _ in range(size)]
        self.start = (0, 0)
        self.end = (size - 1, size - 1)

    def generate_maze(self, percent_walls):
        num_walls = int((percent_walls / 100) * (self.size ** 2))

        for _ in range(num_walls):
            x, y = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
            self.maze[x][y] = '▓'

    def generate_recursive_backtracking_maze(self):
        stack = [(0, 0)]
        visited = set([(0, 0)])

        while stack:
            x, y = stack[-1]
            neighbors = [(x+2, y), (x-2, y), (x, y+2), (x, y-2)]
            neighbors = [(nx, ny) for nx, ny in neighbors if 0 <= nx < self.size and 0 <= ny < self.size and (nx, ny) not in visited]
            
            if neighbors:
                nx, ny = random.choice(neighbors)
                mx, my = (x + nx) // 2, (y + ny) // 2
                self.maze[mx][my] = '◌'
                stack.append((nx, ny))
                visited.add((nx, ny))
            else:
                stack.pop()

    def generate_prims_maze(self):
        visited = set([(0, 0)])
        walls = [(x+1, y) for x in range(0, self.size-2, 2) for y in range(0, self.size, 2)] + [(x, y+1) for x in range(0, self.size, 2) for y in range(0, self.size-2, 2)]

        while walls:
            x, y = random.choice(walls)
            walls.remove((x, y))
            neighbors = [(x+2, y), (x-2, y), (x, y+2), (x, y-2)]
            neighbors = [(nx, ny) for nx, ny in neighbors if 0 <= nx < self.size and 0 <= ny < self.size and (nx, ny) in visited]
            
            if neighbors:
                nx, ny = random.choice(neighbors)
                mx, my = (x + nx) // 2, (y + ny) // 2
                self.maze[mx][my] = '◌'
                visited.add((x, y))
                visited.add((nx, ny))

    def generate_randomized_prims_maze(self):
        walls = [(x, y) for x in range(1, self.size-1, 2) for y in range(1, self.size-1, 2)]

        while walls:
            x, y = random.choice(walls)
            walls.remove((x, y))
            neighbors = [(x+2, y), (x-2, y), (x, y+2), (x, y-2)]
            neighbors = [(nx, ny) for nx, ny in neighbors if 0 <= nx < self.size and 0 <= ny < self.size]
            
            if neighbors:
                nx, ny = random.choice(neighbors)
                mx, my = (x + nx) // 2, (y + ny) // 2
                self.maze[mx][my] = '◌'

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

    def find_path_a_star(self):
        open_set = []
        heapq.heappush(open_set, (0, self.start))
        came_from = {self.start: None}
        g_score = {self.start: 0}

        while open_set:
            _, current = heapq.heappop(open_set)

            if current == self.end:
                path = self.reconstruct_path(came_from, current)
                return path

            for neighbor in self.get_neighbors(current):
                tentative_g_score = g_score[current] + 1

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    heapq.heappush(open_set, (tentative_g_score + self.heuristic(neighbor), neighbor))

        return []

    def find_path_dijkstra(self):
        visited = set()
        pq = [(0, self.start)]
        came_from = {self.start: None}

        while pq:
            cost, current = heapq.heappop(pq)

            if current == self.end:
                path = self.reconstruct_path(came_from, current)
                return path

            if current not in visited:
                visited.add(current)

                for neighbor in self.get_neighbors(current):
                    new_cost = cost + 1
                    if neighbor not in visited:
                        heapq.heappush(pq, (new_cost, neighbor))
                        came_from[neighbor] = current

        return []

    def find_path_bfs(self):
        visited = set()
        queue = Queue()
        queue.put(self.start)
        came_from = {self.start: None}

        while not queue.empty():
            current = queue.get()

            if current == self.end:
                path = self.reconstruct_path(came_from, current)
                return path

            for neighbor in self.get_neighbors(current):
                if neighbor not in visited:
                    queue.put(neighbor)
                    visited.add(neighbor)
                    came_from[neighbor] = current

        return []

    def get_neighbors(self, cell):
        x, y = cell
        return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

    def heuristic(self, cell):
        x, y = cell
        return abs(x - self.end[0]) + abs(y - self.end[1])

    def reconstruct_path(self, came_from, current):
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.insert(0, current)
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
                    self.maze[row][col] = 'S'
                elif (row, col) in path:
                    self.maze[row][col] = '◍'
                if (row, col) == self.end:
                    self.maze[row][col] = 'E'

if __name__ == "__main__":
    size = int(input("Enter the size of the maze: "))
    percent_walls = int(input("Enter the percentage of walls (0-100): "))

    maze_solver = MazeSolver(size)

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nMaze:")
        maze_solver.print_maze()

        print("\n1. Print the path (DFS)")
        print("2. Generate another puzzle")
        print("3. Find path using A* algorithm")
        print("4. Find path using Dijkstra's algorithm")
        print("5. Find path using BFS")
        print("6. Exit the Game")

        user_choice = input("Enter your choice (1/2/3/4/5/6): ")

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
            path = maze_solver.find_path_a_star()
            maze_solver.print_path(path)
            if path:
                print("\nPath:")
                maze_solver.mark_path_on_maze(path)
        elif user_choice == "4":
            path = maze_solver.find_path_dijkstra()
            maze_solver.print_path(path)
            if path:
                print("\nPath:")
                maze_solver.mark_path_on_maze(path)
        elif user_choice == "5":
            path = maze_solver.find_path_bfs()
            maze_solver.print_path(path)
            if path:
                print("\nPath:")
                maze_solver.mark_path_on_maze(path)
        elif user_choice == "6":
            break
        else:
            print("Invalid choice. Please enter a valid option.")
