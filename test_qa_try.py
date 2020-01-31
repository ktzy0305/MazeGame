import mock
import pytest
from MazeCode.mazegame_code import *

@pytest.yield_fixture
def try_input():
    with mock.patch('MazeCode.mazegame_code.check_option') as m:
        yield m

def test_my_input(try_input):
    try_input.return_value = '1'
    assert check_option() == "Option 1 selected"

def test_input():
    with mock.patch('builtins.input', return_value="0"):
        assert check_option() == "Exiting..."
