import pytest
from MazeCode.mazegame_code import *


emptyList = []
mazeList = ["X","O","A","B"]
notmazeList = ["1","2"]

def test_arraylist_empty():
    errorMsg = check_List(emptyList)
    assert errorMsg == "List is empty."

def test_arraylist_notempty():
    errorMsg = check_List(notmazeList)
    assert errorMsg == "List is occupied."
    
def test_arraylist_notempty2():
    errorMsg = check_List(mazeList)
    assert errorMsg == "List is occupied."

def test_List_isMaze():
    errorMsg = checkMaze(mazeList)
    assert errorMsg == "The list is a maze."


def test_List_isNotMaze():
    errorMsg = checkMaze(notmazeList)
    assert errorMsg == "The list is not a maze."
    
