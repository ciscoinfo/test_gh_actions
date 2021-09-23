from functions import get_users

def test_get_users():
    assert get_users() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
