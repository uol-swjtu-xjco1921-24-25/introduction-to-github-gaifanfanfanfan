#maze_skeleton.py
import sys

class Maze:
  """Maze class to store maze state and player position"""
  def __init__(self):
    self.grid = [] # 2D list storing the maze layout (#, space, S, E)
    self.row = 0   # Number of rows in the maze (5-100)
    self.cols = 0  # Number of columns in the maze (5-100)
    self.start = (0,0) #Start Position (row,col)
    self.exit = (0,0)  #Exit position (row,col)
    self.player = (0,0) #Current player position



  def load_maze(filename:str) -> Maze:
    """Load maze file and return a Maze object
    Implement notes:
    -Each line represents a row of the maze
    -Automatically detect positons of S and E
    -Store the original grid data
    """
    maze = Maze()
    # Steps to implement
    # Read the file and fill in maze.grid
    # Set maze.rows and maze.cols
    # Find and verify the existence and uniqueness of S and E
    return maze
