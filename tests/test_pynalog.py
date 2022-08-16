from pynalog import __version__


def test_version():
    assert __version__ == "0.1.0"


def test_pynalog():
    from pynalog import test

    test()


def test_pynalog2():
    import pynalog as plog

    plog.test()
