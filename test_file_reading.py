import pytest
from MazeCode.mazegame_code import *

def test_read_success():
    errorMsg = displayList()
    assert errorMsg == "Success!"

def test_read_failure():
    errorMsg = displayList()
    assert errorMsg == "No list found"
