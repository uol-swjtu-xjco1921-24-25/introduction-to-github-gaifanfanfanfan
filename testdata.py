import subprocess
import os

TEST_MAZE_DIR = "test_data/mazes"
TEST_INPUT_DIR = "test_data/inputs"


def run_test(maze_file, input_file=None,expected_errors=[]):
  """"""
  cmd = ['./maze',maze_file]

  #
  input_data = None
  if input_file:
    with open(input_file,'r') as f:
      input_data = f.read()
  # 
  result = subprocess.run(
    cmd,
    input=input_data,
    capture_output=True,
    text=True,
    timeout=5
  )
  #
  output = result.stdout + result.stderr
  for keyword in expected_errors:
    if keyword not in output:
      raise AssertionError(f"Expected error '{keyword}'not found in output")
    
  return result

"""

"""

def test_valid_maze_normal_win():
  """"""
  maze = os.path.join(TEST_MAZE_DIR,"valid/simple.txt")
  input = os.path.join(TEST_INPUT_DIR, "normal_win.txt")
  result = run_test(maze,input)
  assert "Congratulations" in result.stdout

def test_invalid_characters():
  """"""
