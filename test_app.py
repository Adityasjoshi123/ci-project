import app

def test_add():
    assert app.add(2, 3) == 5
    assert app.add(2, 5) == 7
    assert app.add(8, 1) == 9
    assert app.add(7, 1) == 8

