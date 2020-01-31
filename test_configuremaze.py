import pytest
# from MazeCode.mazegame_code import *

def test_display_configuration_menu():
    message = displayConfigurationMenu()
    assert message == "Displaying Configuration Menu"
     
def test_no_maze_loaded():
    MazeCode.mazegame_code.maze = []
    createWall(1,1)
    assert "No maze is loaded" in ValueError

def test_create_wall():
    createWall(1,1)
    assert MazeCode.mazegame_code.maze[0][0] == "X"

def test_create_passageway():
    createPassageWay(2,2)
    assert MazeCode.mazegame_code.maze[1][1] == "O"

def test_create_start_point():
    createStartPoint(2,3)
    assert MazeCode.mazegame_code.maze[1][2] == "A"

def test_create_end_point():
    createEndPoint(5,6)
    assert MazeCode.mazegame_code.maze[4][5] == "B"

def test_coordinate_input_out_of_range():
    createPassageWay(-1,-1)
    assert "Coordinate Out Of Range" in ValueError

def test_return_to_configuration_menu():
    enterCreateWallMenu()
    message = exitToConfigurationMenu()
    assert message == "Exit to Configuration Menu"

def test_exit_to_main_menu_from_configuration_option():
    enterCreateWallMenu()
    message = exitToMainMenu()
    return message == "Exit to Main Menu"