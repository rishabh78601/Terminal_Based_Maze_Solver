# 🌐 Terminal-Based Maze Solver 🧩

A terminal-based application that generates a random maze, finds a path from the start to the end, and visualizes the maze and path in the terminal.

## Table of Contents
- 📚 [Prerequisites](#prerequisites)
- 🛠️ [Installation](#installation)
- 🚀 [Usage](#usage)
- 🧰 [Code Components](#code-components)
- 🖼️ [Sample Output](#sample-output)
- 🔮 [Future Perspective](#future-perspective)
- 😎 [Emojis](#emojis)

## Prerequisites
- 🧠 Basic understanding of arrays and loops.
- 🖥️ Familiarity with terminal-based input/output.

## Installation
1. Clone the repository: `git clone https://github.com/your-username/terminal-maze-solver.git`
2. Navigate to the project directory: `cd terminal-maze-solver`
3. Run the program: `python main.py` (replace `python` with your Python interpreter if needed).

## Usage
1. Enter the size of the maze when prompted.
2. Choose to print the path, generate another puzzle, or exit the game.

## Code Components
### Libraries
- 🎲 `random`: Used for generating random numbers for maze generation.
- 🖥️ `os`: Used for clearing the terminal screen ('cls' for Windows, 'clear' for Unix-like systems).
- ⚙️ `heapq`: Used for the priority queue in A* and Dijkstra's algorithms.
- 🧱 `queue`: Used for the queue in BFS.

### Maze Generation Algorithms
1. Recursive Backtracking
2. Prim's Algorithm
3. Randomized Prim's Algorithm

### Pathfinding Algorithms
1. Depth-First Search (DFS)
2. A* Algorithm
3. Dijkstra's Algorithm
4. Breadth-First Search (BFS)

### Data Structures Used
1. **Stack:** Used in the Recursive Backtracking maze generation algorithm.
2. **Set:** Used for tracking visited cells in maze generation and pathfinding.
3. **Priority Queue (Heap):** Used for the open set in A* and Dijkstra's algorithms.
4. **Queue:** Used for BFS algorithm.
5. **Heuristic Function:** Manhattan Distance.

### Code Structure
- Maze Generation Function
- Maze Printing Function
- Pathfinding Function
- Path Printing Function
- Path Marking Function

## Sample Output
The maze is visualized in the terminal with distinct characters or colors for:
- Start (S) and End (E)
- Walls: ▓ (red)
- Open Space: ◌ (blue)
- Path: ◍ (green)

## Future Perspective
- Additional maze generation algorithms:
  1. Recursive Backtracking Algorithm
  2. Prim's Algorithm
  3. Randomized Prim's Algorithm
- Additional pathfinding algorithms for comparison:
  1. A* Algorithm
  2. Dijkstra's Algorithm
  3. Breadth-First Search (BFS)
