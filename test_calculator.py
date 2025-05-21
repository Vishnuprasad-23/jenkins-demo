from calculator import add, subtract

def test_add():
    assert add(1,2) == 3

def test_subtract():
    assert subtract(5,3) == 2

def test_add_fail():
    assert add(2,6) == 8