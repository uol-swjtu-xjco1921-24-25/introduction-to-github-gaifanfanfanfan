import subprocess
import os

TEST_MAZE_DIR = "test_data/mazes"
TEST_INPUT_DIR = "test_data/inputs"


def run_test(maze_file, input_file=None,expected_errors=[],excepted_output=[]):
  """generic test execution function"""
  cmd = ['./maze',maze_file]

  #read input commands
  input_data = None
  if input_file:
    with open(os.path.join(TEST_INPUT_DIR,input_file),'r') as f:
      input_data = f.read()
  # Execute test
  result = subprocess.run(
    cmd,
    input=input_data,
    capture_output=True,
    text=True,
    timeout=5
  )
  #validate output
  output = result.stdout + result.stderr
  for keyword in expected_errors:
    if keyword not in output:
      raise AssertionError(f"Expected error '{keyword}'not found in output")
  for content in excepted_output:
    if content.lower() not in output.lower():
      raise AssertionError(f"Expected content '{content}' not found")
  return result


"""
 Specific test cases
"""

def test_valid_maze_normal_win():
  """Test normal successful maze completion"""
  maze = os.path.join(TEST_MAZE_DIR,"valid/simple.txt")
  input = os.path.join(TEST_INPUT_DIR, "normal_win.txt")
  result = run_test(maze,input)
  assert "Congratulations" in result.stdout

def test_invalid_characters():
  """Test detection of invalid characters"""
  maze = os.path.join(TEST_MAZE_DIR,"Z.txt")
  run_test(maze,expected_errors=["Invalid character 'Z' "])

def test_bound_movement():
  """Test movement attempts beyond maze boundaries"""
  maze = os.path.join(TEST_MAZE_DIR,"3.txt")
  inputs = os.path.join(TEST_MAZE_DIR,"3.txt")
  result = run_test(maze,inputs)
  assert "out of bounds" in result.stdout

def test_oversized_maze():
  """test maze file exceeding maximum allowed dimension"""
  maze = os.path.join(TEST_MAZE_DIR,"4.txt")
  run_test(maze,expected_errors=["excceds maximum size "])

if __name__ == "__main__":
  test_oversized_maze()
  test_bound_movement()
  test_invalid_characters()


 


