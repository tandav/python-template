import mypackage


def test_smoke():
    assert hasattr(mypackage, '__version__')
