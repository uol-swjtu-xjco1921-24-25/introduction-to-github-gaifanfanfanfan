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
def validate_maze(maze: Maze)-> bool:
    """Validate the maze structure
    Validation rules:
    -Must be rectangular (all rows of equal length)
    -Size must be 5 <= rows <= 100 and 5 <= cols <= 100
    -Must contain one unique S and one unique E
    """
    # Example:
    # if maze.row<5 or maze.rows>100: raise error
    # Check each row length equals maze.col
    return True
def move_player(maze: Maze, direction:str) -> bool:
  """Handle player movement
  Movement rules:
  - Compute new position based on WASD
  - Check wall collision or out of bound moves
  - Update player position
  - Trigger game over if E is reached
  """
  #Examplles:
  #new_row = maze.player[0] + (direction=='w' ? -1 : 1)
  #Check if maze.grid[new_row][new_row]is#
  # Ensure 0 <= row < rows
  return True #Return whether the move is successful

def display_map(maze: Maze):
  """
  Display the map player position
  Display rules:
  - Show X at player's current location
  - Keep original S and E characters
  """
  # Implementation:
  # Loop over maze.grid, show X at maze.player
  # Show original characters otherwise

  print("Map displays successfully")




def handle_input(maze: Maze, command:str)-> bool:
  """Handle user input
  Input rules:
  - Case-insensitive command handling
  - Handle move/map/quit commands
  - Show message on invalid moves
  """
  cmd = command.lower()
  if cmd == 'q':
    return False
  elif cmd == 'm':
    display_map(maze)
  elif cmd in ('W','A','S','D'):
    if not move_player(maze,cmd):
      print("Invalid move")
  else:
    print("invalid command")
  return True


def main():
  if len(sys.argv) != 2:
    print('Usage:python maze.py <maze_file>')
    sys.exit(1)

  try:
    maze = load_maze(sys.argv[1])
    if not validate_maze(maze):
      raise ValueError("Maze validation failed")
    print("Game start! Use WASD to move, M to view map, Q to quit")
    while True:
      cmd = input(">").strip()
      if not handle_input(maze,cmd):
        print("Game exited")
        break
      if maze.player == maze.exit:
        print("Congratulations! You escapsed the maze!") 
        display_map(maze)
        break

  except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)


if __name__ == "__main__":
  main()