from jabbapylib.mouse import mouse


def test_get_pos():
    result = mouse.get_pos()
    assert isinstance(result, tuple) and len(result) == 2


def test_move_to():
    backup = mouse.get_pos()
    TO = (100, 100)
    mouse.move_to(TO)
    assert mouse.get_pos() == TO
    mouse.move_to(backup)