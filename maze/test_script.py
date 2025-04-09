import subprocess
import os

TEST_MAZE_DIR = ""
TEST_INPUT_DIR = ""


def run_test(maze_file, input_file=None,expected_errors=[],excepted_output=[]):
  """generic test execution function"""
  cmd = ['./maze',maze_file]

  #read input commands
  input_data = None
  if input_file:
    file_path = os.path.join(TEST_INPUT_DIR, input_file)
    print(f"Attempting to open file: {file_path}")  # 打印出完整路径
    with open(file_path, 'r') as f:
        input_data = f.read()
  # Execute test
  print(f"Looking for file: {os.path.join(TEST_INPUT_DIR, input_file)}")
  try:
    result = subprocess.run(
    cmd,
    input=input_data,
    capture_output=True,
    text=True,
    timeout=30
    
  )
  except subprocess.TimeoutExpired:
    raise AssertionError("Test timed out after 30 second")

  
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
  maze = os.path.join(TEST_MAZE_DIR,"test_data/mazes/valid/simple.txt")
  input = os.path.join(TEST_INPUT_DIR, "test_data/inputs/valid/normal_win.txt")
  result = run_test(maze,input)
  
  assert "Congratulations" in result.stdout + result.stderr

def test_invalid_characters():
  """Test detection of invalid characters"""
  maze = os.path.join(TEST_MAZE_DIR,"test_data/mazes/invalid/invalid_char.txt")
  run_test(maze,expected_errors=["Invalid character 'Z'"])

def test_bound_movement():
  """Test movement attempts beyond maze boundaries"""
  maze = os.path.join(TEST_MAZE_DIR,"test_data/mazes/valid/bound_test.txt")
  inputs = os.path.join(TEST_MAZE_DIR,"test_data/inputs/valid/boundary_test.txt")
  result = run_test(maze,inputs)
  assert "out of bounds" in result.stdout + result.stderr

def test_oversized_maze():
  """test maze file exceeding maximum allowed dimension"""
  maze = os.path.join(TEST_MAZE_DIR,"test_data/mazes/invalid/oversize.txt")
  run_test(maze,expected_errors=["excceds maximum size"])

def test_invalid_start_position():
  """Test invalid starting position"""
  maze = os.path.join(TEST_MAZE_DIR,"test_data/mazes/invalid/no_start.txt")
  run_test(maze,expected_errors=["Invalid start position"])

def test_small_maze():
  """Test detection of maze smaller than minimum allowed size"""
  maze = os.path.join(TEST_MAZE_DIR,"test_data/mazes/invalid/smallmaze.txt")
  run_test(maze,expected_errors=["Maze size is too small", "Minimum size is 5"])



def test_multiple_start_position():
  """Test handing of multiple entry points"""
  maze = os.path.join(TEST_MAZE_DIR,"test_data/mazes/invalid/multi_start.txt")
  result = run_test(maze , excepted_output=["multiple entry"])
  assert "S" in result.stdout + result.stderr

def test_uneven_maze_rows():
  """test maze with inconsistent row lengths"""
  maze = os.path.join(TEST_MAZE_DIR, "test_data/mazes/invalid/uneven_rows.txt")
  run_test(maze,expected_errors=["row or column should be the same length"])

def test_missing_maze_file():
  """Test behavior when maze file does not exist"""
  maze = os.path.join(TEST_MAZE_DIR, "non_existent_maze.txt")  
  try:
    run_test(maze)  
    raise AssertionError("Expected error due to missing maze file, but test passed")
  except FileNotFoundError:
    pass
  result = run_test(maze)
  assert "File not found" in (result.stdout + result.stderr)  




def test_1_normal_win():
  """success1"""
  maze = os.path.join(TEST_MAZE_DIR,"test_data/mazes/valid/complex.txt")
  inputs = os.path.join(TEST_MAZE_DIR,"test_data/inputs/valid/mixed_case.txt")
  result = run_test(maze,inputs)
  assert result.returncode == 0
def test_2_normal_win():
  """success2"""
  maze = os.path.join(TEST_MAZE_DIR,"test_data/mazes/valid/complex2.txt")
  inputs = os.path.join(TEST_MAZE_DIR,"test_data/inputs/valid/complex2.txt")
  result = run_test(maze,inputs)
  assert result.returncode == 0

def test_3_partial_path():
  """Test that partial path results in Quit message"""
  maze = os.path.join(TEST_MAZE_DIR,"test_data/mazes/valid/simple.txt")
  inputs = os.path.join(TEST_MAZE_DIR,"test_data/inputs/valid/partial_path.txt")
  result = run_test(maze,inputs)
  assert "Quit" in result.stdout + result.stderr

def test_4_map_reveal():
  """Test that map is correctly revealed upon user command"""
  maze = os.path.join(TEST_MAZE_DIR, "test_data/mazes/valid/simple.txt")
  result = run_test(
    maze,
    input_file="valid/map.txt",  
    excepted_output=["#", "X", "E", "S", ""]  
  )
  
  

def test_5_wall_collision():
  """Test movement attempts collision wall"""
  
  maze = os.path.join(TEST_MAZE_DIR, "test_data/mazes/invalid/wall_crash.txt")
  input_file = os.path.join(TEST_INPUT_DIR, "test_data/inputs/invalid/wall_crash.txt")
  result = run_test(
    maze,
    input_file,  
    expected_output=["cannot move","position remains"]
  )
  

def output_contains(output,*keywords):
  missing = [k for k in keywords if k.lower() not in output.lower()]
  if missing:
    raise AssertionError(f"Missing expected keywords:{missing}")

if __name__ == "__main__":
 
 test_valid_maze_normal_win()
 test_invalid_characters()
 test_bound_movement()
 test_oversized_maze()
 test_invalid_start_position()
 test_small_maze()
 test_multiple_start_position()
 test_uneven_maze_rows()
 test_missing_maze_file()
 test_1_normal_win()
 test_2_normal_win()
 test_3_partial_path()
 test_4_map_reveal()
 test_5_wall_collision()


