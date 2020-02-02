import pytest
# from MazeCode.mazegame import *
from MazeCode import mazegame
from MazeCode.mazegame import *

def test_display_configuration_menu():
    message = displayConfigurationMenu()
    assert message == "Displaying Configuration Menu"
     
def test_no_maze_loaded():
    mazegame_code.maze = []
    with pytest.raises(GameError) as e:
        createWall(1,1)
    assert "No maze is loaded" in str(e.value)

def test_create_wall():
    check_filename("Maze.csv")
    createWall(1,1)
    assert mazegame_code.maze[0][0] == "X"

def test_create_passageway():
    check_filename("Maze.csv")
    createPassageWay(2,2)
    assert mazegame_code.maze[1][1] == "O"

def test_create_start_point():
    check_filename("Maze.csv")
    createStartPoint(2,3)
    assert mazegame_code.maze[1][2] == "A"

def test_create_end_point():
    check_filename("Maze.csv")
    createEndPoint(5,6)
    assert mazegame_code.maze[4][5] == "B"

def test_coordinate_input_out_of_range():
    check_filename("Maze.csv")
    with pytest.raises(GameError) as e:
        createPassageWay(-1,-1)
        assert "Invalid Row Value" in str(e.value)

def test_return_to_configuration_menu():
    value = handle_configuration_option_input("B", createWall)
    assert value == False

def test_exit_to_main_menu_from_configuration_option():
    enterCreateWallMenu()
    message = exitToMainMenu()
    return message == "Exit to Main Menu"
    value = handle_configuration_option_input("M", createWall)
    assert value == True
