# Terminal-Based-Maze-Solver

## Objective:
Develop a terminal-based application that generates a random maze, finds a path from the start to the end, and visualizes the maze and path in the terminal.

## Prerequisites:
- Basic understanding of arrays and loops.
- Familiarity with terminal-based input/output.

## Specifications:

### Input:
- Size of the maze (n).
- Users choose to either print the path, generate another puzzle, or exit the game.

### Output:
- A visual representation of the generated maze in the terminal (2D n x n array).
- A visual representation of the path from start to end, if it exists.

## Code Components:

### Libraries:
1. `random`: Used for generating random numbers for maze generation.
2. `os`: Used for clearing the terminal screen ('cls' for Windows, 'clear' for Unix-like systems).
3. `heapq`: Used for the priority queue in A* and Dijkstra's algorithms.
4. `queue`: Used for the queue in BFS.

### Maze Generation Algorithms:
1. Recursive Backtracking
2. Prim's Algorithm
3. Randomized Prim's Algorithm

### Pathfinding Algorithms:
1. Depth-First Search (DFS)
2. A* Algorithm
3. Dijkstra's Algorithm
4. Breadth-First Search (BFS)

### Data Structures Used:
1. **Stack:**
   - Used in the Recursive Backtracking maze generation algorithm.
   - Used implicitly in DFS pathfinding.
2. **Set:**
   - Used for tracking visited cells in maze generation and pathfinding.
3. **Priority Queue (Heap):**
   - Used for the open set in A* and Dijkstra's algorithms.
   - Implemented using the heapq library.
4. **Queue:**
   - Used for BFS algorithm.
   - Implemented using the queue library.
5. **Heuristic Function:**
   - Manhattan Distance: Used as a heuristic in the A* algorithm. It calculates the sum of the absolute differences of the x and y coordinates between two points.

### Code Structure:
- **Maze Generation Function:**
  - Generates a random maze and returns it as an array.
- **Maze Printing Function:**
  - Prints the maze in the terminal.
- **Pathfinding Function:**
  - Finds a path from the start to the end using a suitable algorithm like BFS or DFS.
- **Path Printing Function:**
  - Prints the path in a readable format.
- **Path Marking Function:**
  - Marks the path on the maze for visualization.

## Sample Output:
The maze should be visualizing in the terminal with distinct characters or colors for:
- Start (S) and End (E)
- Walls: ▓ (red)
- Open Space: ◌ (Blue)
- Path: ◍ (Green)
### Sample Output:
![Maze and Path Output](D:\Downloads\image (1).png)

<!-- Add more details if needed -->

## Future Perspective:
- Implemented additional maze generation algorithms:
  1. Recursive Backtracking Algorithm
  2. Prim's Algorithm
  3. Randomized Prim's Algorithm
- Implemented additional pathfinding algorithms for comparison:
  1. A* Algorithm
  2. Dijkstra's Algorithm
  3. Breadth-First Search (BFS)

