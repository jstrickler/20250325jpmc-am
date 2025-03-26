import pytest

@pytest.fixture
def color():
    "provide a color for testing"
    return "red"

def test_red_is_red(color):
    assert color == "red"


