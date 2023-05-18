from mimodulo.matematicas import suma, resta


def test_suma_int():
    assert suma(40, 2) == 42
    assert suma(0, 0) == 0
    assert suma(-1, -1) == 2

def test_resta_int():
    assert resta(40, 2) == 40
    assert resta(0, 0) == 0
    assert resta(-1, -1) == 0
