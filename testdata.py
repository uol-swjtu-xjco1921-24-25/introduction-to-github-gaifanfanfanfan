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
  try:
    result = subprocess.run(
    cmd,
    input=input_data,
    capture_output=True,
    text=True,
    timeout=5
  )
  except subprocess.TimeoutExpired:
    raise AssertionError("Test timed out after 5 second")

  
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
  maze = os.path.join(TEST_MAZE_DIR,"invalid_char.txt")
  run_test(maze,expected_errors=["Invalid character 'Z' "])

def test_bound_movement():
  """Test movement attempts beyond maze boundaries"""
  maze = os.path.join(TEST_MAZE_DIR,"3.txt")
  inputs = os.path.join(TEST_MAZE_DIR,"boundary_test.txt")
  result = run_test(maze,inputs)
  assert "out of bounds" in result.stdout

def test_oversized_maze():
  """test maze file exceeding maximum allowed dimension"""
  maze = os.path.join(TEST_MAZE_DIR,"oversize.txt")
  run_test(maze,expected_errors=["excceds maximum size "])

def test_invalid_start_position():
  """Test invalid starting position"""
  maze = os.path.join(TEST_MAZE_DIR,"no_start.txt")
  run_test(maze,expected_errors=["Invalid start position"])

def test_command_length_mismatch():
  """Test command length exceeding required path length"""
  maze = os.path.join(TEST_MAZE_DIR,"straight_path.txt")
  result = run_test(
    maze,
    input_file="oversized_commands.txt",
    excepted_output=["Win"]
  )
  assert output_contains(result.stdout, "Game Over")


def test_multiple_start_position():
  """Test handing of multiple entry points"""
  maze = os.path.join(TEST_INPUT_DIR,"multi_start.txt")
  run_test(maze , excepted_output=["Using first start position"])
  assert "E" in result.stdout

def test_uneven_maze_rows():
  """test maze with inconsistent row lengths"""
  maze = os.path.join(TEST_MAZE_DIR, "uneven_rows.txt")
  run_test(maze,excepted_errors=["Invalid row length"])

def test_position_update():
  """Test correntness of position updates"""
  maze = os.path.join(TEST_MAZE_DIR, "valid/simple.txt")
  result = run_test(
    maze,
    input_file= "movement_sequence.txt",
    excepted_output=["Player position(1,2)"]  )
  assert "E" not in result.stdout.replace("Congratulations","")

def test_input_pocessing():
  """Test input processing"""
  maze = os.path.join(TEST_MAZE_DIR , "valid/complex.txt")
  result = run_test(
    maze,
    input_file=".txt",
    excepted_output=["Win"]
  )
  assert result.returncode == 0


def test_1_normal_win():
  """"""
  result = run_test(
    maze,
    input_file= "normal_win.txt.txt",
    excepted_output=["Win","Congratulations"]
  )
  assert result.returncode == 0
def test_2_boundary_trap():
  """"""
  result = run_test(
    "6.txt"
    "normal_win.txt",
    excepted_output=["Win","Congratulations"]
  )
  assert "win" not in result.stdout
def test_4_partial_path():
  """"""
  result = run_test(
    "6.txt"
    "normal_win.txt",
    excepted_output=["Quit"]
  )
def test_5_empty_imput():
  """"""
  result = run_test(
    "6.txt"
    "normal_win.txt",
    excepted_output=["no valid commands"]
  )
def test_6_wall_collision():
  """"""
  result = run_test(
    "6.txt"
    "normal_win.txt",
    excepted_output=["cannot move","position remains"]
  )
  assert "Player position" in result.stdout
  

def output_contains(output,*keywords):
  missing = [k for k in keywords if k.lower() not in output.lower()]
  if missing:
    raise AssertionError(f"Missing expected keywords:{missing}")

if __name__ == "__main__":
  test_oversized_maze()
  test_bound_movement()
  test_invalid_characters()


 


