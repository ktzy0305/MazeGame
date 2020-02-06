import pytest
from MazeCode.mazegame import *


maze = [
['O', 'O', 'X', 'A'],
['X', 'X', 'O', 'O'],
['B', 'O', 'O', 'X'],
['X', 'X', 'X', 'X']]

num= 2,2

check_filename('play_maze_test.csv')

def test_add_list():
    check_filename('play_maze_test.csv')
    
    
def test_error_inputation1(): #testcase 1
    result = move("1", num)
    assert result == "Invalid Movement. Please try again."

def test_error_inputation2(): #testcase 1
    result = move("z", num)
    assert result == "Invalid Movement. Please try again."

def test_error_inputation3(): #testcase 1
    result = move("@", num)
    assert result == "Invalid Movement. Please try again."

def test_error_inputation4(): #testcase 1
    result = move("12as%^", num)
    assert result == "Invalid Movement. Please try again."

def test_upward_movement(): #testcase 2
    check_filename('play_maze_test1.csv')
    result = move("W", (2,2))
    check_option("2")
    assert result == "Moved upwards"

def test_downward_movement(): #testcase 3
    result = move("S", (1,2))
    assert result == "Moved downwards"

def test_left_movement(): #testcase 4
    result = move("A", (2,2))
    assert result == "Moved left"

def test_right_movement(): #testcase 5
    result = move("D", (2,1))
    assert result == "Moved right"

def test_wall_blockage(): #testcase 6
    result = move("D", num)
    assert result == "Wall ahead"
    
def test_menu_exit(): #testcase 7
    result = move("M", num)
    assert result == False

def test_wall_existing():#testcase 8
    result = SpaceCheck("X")
    assert result == "Wall"
    
def test_free_space():#testcase 9
    result = SpaceCheck("O")
    assert result == "Space"

def test_ending(): #9.1
    result = SpaceCheck("B")
    assert result == "End"

    
def test_current_location():#testcase 10
    result = current_location([['X','O','O','A','O','O','X']])
    assert result == (0, 3)

def test_end_location():#testcase 11
    result = end_location([['X','B','O','A','O','O','X']])
    assert result == (0, 1)

def test_case_sensitive():#testcase 12
    result = move("w", num)
    assert result == "Moved upwards"

def test_moving_out_up():#testcase 13
    result = move("w", (0,2))
    assert result == "Invalid Movement. Please try again."

def test_moving_out_side():#testcase 13
    result = move("D", (0,3))
    assert result == "Invalid Movement. Please try again."

def test_return_menu():#testcase 14
    result = move("M")
    assert result == False

