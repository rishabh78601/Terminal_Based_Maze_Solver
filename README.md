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
  
## Rules:
<li>The maze is represented as an array where each cell can be either a wall or an open space.
<li>The top-left corner is the start (S), and the bottom-right corner is the end (E).
<li>The application should provide options to print the path, generate another puzzle, or exit the game.
<li>The number of random walls should be restricted to be less than or equal to % of the total cells to increase the likelihood of a solvable maze.
  
## Guidelines:
<li>Generate a random maze of size n with walls and open spaces.
<li>Implement a pathfinding algorithm to find a path from the start to the end.
<li>Visualize the maze and the path in the terminal.
<li>Provide options to the user for further actions.
  
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
