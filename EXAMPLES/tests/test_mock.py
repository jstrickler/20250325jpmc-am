import pytest
import spamlib
from spamlib.spam import Spam
from datetime import datetime

@pytest.fixture
def datetime_now():
    return datetime.now()

@pytest.fixture
def ham_value():
    return 42

@pytest.fixture
def ham_result(ham_value):  # use ham_value fixture
    return ham_value * 10

def test_spam_calls_ham(mocker, ham_value, ham_result):
    # need to patch spamlib.spam.ham, not hamlib.ham
    mocker.patch("spamlib.spam.ham", return_value=ham_value * 10)
    s = Spam(ham_value)  # Create instance of Spam, which calls ham()
    assert s.value == ham_result
    assert spamlib.spam.ham.calledoncewith(ham_value)

def test_spam_has_current_time(mocker, datetime_now):
    mock_datetime = mocker.patch(
        "spamlib.spam.datetime",
    )
    mock_datetime.return_value = datetime_now
    s = Spam(10)
#    assert s.current_time == datetime_now
