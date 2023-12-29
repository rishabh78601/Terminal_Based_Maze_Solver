# Terminal-Based-Maze-Solver
Objective:
Develop a terminal-based application that generates a random maze, finds a path from the start to the end, and visualizes the maze and path in the terminal.

## Prerequisites:
<li>Basic understanding of arrays and loops.
<li>Familiarity with terminal-based input/output.
  
# Specifications:

## Input:
<li>Size of the maze (n).
<li>Users choose to either print the path, generate another puzzle, or exit the game.
  
## Output:
<li>A visual representation of the generated maze in the terminal (2D n x n array).
<li>A visual representation of the path from start to end, if it exists.
  
# The code uses several libraries, algorithms, and data structures. Here's a breakdown:

## Libraries:
  1.	random: Used for generating random numbers for maze generation.
  2.	os: Used for clearing the terminal screen ('cls' for Windows, 'clear' for Unix-like systems).
  3.	heapq: Used for the priority queue in A* and Dijkstra's algorithms.
  4.	queue: Used for the queue in BFS.

## Algorithms:
  ### 1.	Maze Generation Algorithms:
   <li>	Recursive Backtracking
   <li>Prim's Algorithm
   <li>Randomized Prim's Algorithm
  
  ### 2.	Pathfinding Algorithms:
   <li>Depth-First Search (DFS)
   <li>A* Algorithm
   <li>Dijkstra's Algorithm
   <li>Breadth-First Search (BFS)

##Data Structures Used:
  1. Stack:
   <li>Used in the Recursive Backtracking maze generation algorithm.
   <li>Used implicitly in DFS pathfinding.
  2. Set:
   <li>Used for tracking visited cells in maze generation and pathfinding.
  3. Priority Queue (Heap):
   <li>Used for the open set in A* and Dijkstra's algorithms.
   <li>Implemented using the heapq library.
  4. Queue:
   <li>Used for BFS algorithm.
   <li>Implemented using the queue library.
  5. Heuristic Function:
   <li>Manhattan Distance:
   Used as a heuristic in the A* algorithm. It calculates the sum of the absolute differences of the x and y coordinates 
   between two points.

     Note:
<li>The code demonstrates a variety of maze generation and pathfinding techniques.
<li>It provides flexibility for adding new algorithms or modifying existing ones.
<li>A* and Dijkstra's algorithms use a priority queue for efficient exploration of the search space.
<li>BFS uses a simple queue for breadth-first exploration.
  
## Code Structure:
<li>Maze Generation Function:
Generates a random maze and returns it as an array.

<li>Maze Printing Function:
Prints the maze in the terminal.

<li>Pathfinding Function:
Finds a path from the start to the end using a suitable algorithm like BFS or DFS.

<li>Path Printing Function:
Prints the path in a readable format.

<li>Path Marking Function:
Marks the path on the maze for visualization.

## Sample Output:
The maze should be visualized in the terminal with distinct characters or colors for:

<li>Start (S) and End (E)
<li>Walls: ▓ (red)
<li>Open Space: ◌ (Blue)
<li>Path: ◍ (Green)

##Future Perspective:
<li>Implemented additional maze generation algorithms.
  1. Recursive Backtracking Algorithm:
  2. Prim's Algorithm:
  3. Randomized Prim's Algorithm:
<li>Implemented additional pathfinding algorithms for comparison.
  1. A Algorithm:*
  2. Dijkstra's Algorithm:
  3. Breadth-First Search (BFS):

