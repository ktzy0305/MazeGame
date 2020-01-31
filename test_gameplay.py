import pytest
from MazeCode.mazegame_code import *

def test_error_inputation1(): #testcase 1
    result = move("1")
    assert result == "Invalid Movement. Please try again."

def test_error_inputation2(): #testcase 1
    result = move("z")
    assert result == "Invalid Movement. Please try again."

def test_error_inputation3(): #testcase 1
    result = move("@")
    assert result == "Invalid Movement. Please try again."

def test_error_inputation4(): #testcase 1
    result = move("12as%^")
    assert result == "Invalid Movement. Please try again."

def test_upward_movement(): #testcase 2
    result = move("W")
    assert result == "Moved upwards"

def test_downward_movement(): #testcase 3
    result = move("S")
    assert result == "Moved upwards"

def test_left_movement(): #testcase 4
    result = move("A")
    assert result == "Moved upwards"

def test_right_movement(): #testcase 5
    result = move("D")
    assert result == "Moved upwards"

def test_wall_blockage(): #testcase 6
    result = move("A")
    assert result == "Invalid Movement. Please try again."
    
def test_menu_exit(): #testcase 7
    result = move("M")
    assert result == "Exiting to Menu"

def test_wall_existing():#testcase 8
    result = SpaceCheck("X")
    assert result == "Wall"
    
def test_free_space():#testcase 9
    result = SpaceCheck("O")
    assert result == "Space"
    
def test_current_location():#testcase 10
    result = current_location("[X,O,O,A,O,O,X]")
    assert result == "Row1, Column3"
    
def test_case_sensitive():#testcase 11
    result = move("a")
    assert result == "Moved upwards"
