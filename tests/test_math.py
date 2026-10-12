from main import add


def test_addition():
    assert add(2, 3) == 5


def test_addition_with_negative_number():
    assert add(-2, 3) == 1
