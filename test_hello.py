from hello import product


def test_product():
    assert product(5, 2) == 10
    assert product(-8, -1) == 8
    assert product(0, 1) == 0
    assert product(4, -5) == -20
