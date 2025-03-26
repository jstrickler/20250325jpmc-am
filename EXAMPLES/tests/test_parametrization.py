import pytest

def triple(x):  # Function to test
    return x * 3

test_data = [(5, 15), (0, 0), (-1, -3), ('a', 'aaa'), ([True], [True, True, True])]  # List of values for testing containing input and expected result


@pytest.mark.parametrize("input,expected", test_data)  # Parametrize the test with the test data; the first argument is a string defining parameters to the test and mapping them to the test data
def test_triple(input, expected):  # The test expects two parameters (which come from each element of test data)
    # print("input {} result {}:".format(input, result))  # The test expects two parameters (which come from each element of test data)
    assert triple(input) == expected   # Test the function with the parameters
