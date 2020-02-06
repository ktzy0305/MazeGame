import pytest
from MazeCode.mazegame import*
import csv
result = ""

def test_filenameinput():
    result = check_filename("maze.csv")
    assert result == "Filename correct"

def test_filename_exact():
    result = check_filename("Maze.csv")
    assert result == "Filename correct"

def test_filename_case_sensitive():
    result = check_filename("MAZE.CSV")
    assert result == "Filename correct"

def test_filename_invalid():
    result = check_filename("dssdfsdf")
    assert result == "Filename incorrect"
