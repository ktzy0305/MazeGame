import pytest
import builtins
from MazeCode.mazegame import *

def test_invalid_display_menu(): #test case 1
    result = display_menu(False)
    assert result == "Invalid menu"
    
def test_display_menu(): #test case 2
    result = display_menu(True)
    assert result == "Displaying Menu"
    
def  test_invalid_option_input(): #test case 3
    result = check_option("5")
    assert result == "Invalid Option"
  
def  test_alphabet_input(): #test case 4
    result = check_option("abc")
    assert result == "Invalid Option"
    
def  test_symbols_input(): #test case 5
    result = check_option("@")
    assert result == "Invalid Option"
    
def  test_double_digits_input(): #test case 6
    result = check_option("92")
    assert result == "Invalid Option"
    
def test_option1(): #test case 7
    result = check_option("1", "break")
    assert result == "Option 1 selected"
    
def test_option2(): #test case 8
    result = check_option("2")
    assert result == "Option 2 selected"
    
def test_option3(): #test case 9
    result = check_option("3", "break")
    assert result == "Option 3 selected"
    
def test_option4(): #test case 10
    result = check_option("4", "break")
    assert result == "Option 4 selected"
    
def test_option0(): #test case 11
    result = check_option("0")
    assert result == False
    

