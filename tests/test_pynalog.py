def test_pynalog():
    from pynalog import test

    test()


def test_pynalog2():
    import pynalog as plog

    plog.test()


def test_plogsum():
    import pynalog as plog

    mysum = plog.plogsum(10)
