import pytest
from MazeCode.mazegame_code import*

def test_filenameinput():
    result = check_filename("maze.csv")
    assert results == "Filename correct"

def test_filenameinput2():
    result = check_filename("MAZE.CSV")
    assert results == "Filename incorrect"
