from color.beaker import Beaker


def test_pour_into_self():
    a = Beaker(['b', 'o', 'r'])
    b = a._content[0]
    o = a._content[1]
    r = a._content[2]

    bs = a._content[0].size
    os = a._content[1].size
    rs = a._content[2].size

    size = len(a._content)
    a.pour_into(a)
    assert len(a._content) == size

    assert a._content[0] == b
    assert a._content[1] == o
    assert a._content[2] == r

    assert a._content[0].size == bs
    assert a._content[1].size == os
    assert a._content[2].size == rs


def test_insert_more_than_size():
    try:
        a = Beaker(['b', 'o', 'o', 'r', 'g'])
    except Exception:
        pass
    else:
        assert False


def test_pour_into_empty():
    a = Beaker(['b', 'o', 'o', 'r'])
    b = Beaker()

    len_a = len(a)
    len_b = len(b)
    shift = a.top.size

    a.pour_into(b)

    assert len(a) + len(b) == len_a + len_b
    assert len(a) == len_a - shift
    assert len(b) == len_b + shift


def test_pour_empty_into_full():
    a = Beaker()
    b = Beaker(['b', 'o', 'o', 'r'])

    len_a = len(a)
    len_b = len(b)

    a.pour_into(b)

    assert len(a) == len_a
    assert len(b) == len_b


def test_top_values_different():
    """
    Should raise error
    """
    a = Beaker(['b', 'o', 'o', 'r'])
    b = Beaker(['o', 'o', 'r'])

    len_a = len(a)
    len_b = len(b)
    shift = 0

    try:
        a.pour_into(b)
    except ValueError:
        pass
    else:
        assert False

    assert len(a) + len(b) == len_a + len_b
    assert len(a) == len_a - shift
    assert len(b) == len_b + shift


def test_less_space_than_reqd():
    """
    Same adjacent values are transfered simultaneously
    """
    a = Beaker(['o', 'o', 'r'])
    b = Beaker(['o', 'o', 'r'])

    len_a = len(a)
    len_b = len(b)
    shift = 0

    try:
        a.pour_into(b)
    except ValueError:
        pass
    else:
        assert False

    assert len(a) + len(b) == len_a + len_b
    assert len(a) == len_a - shift
    assert len(b) == len_b + shift


def test_different_sized_beakers():
    a = Beaker(['o', 'o', 'r'])
    b = Beaker(['o', 'o', 'r'], 5)

    len_a = len(a)
    len_b = len(b)
    shift = a.top.size
    b_top_size = b.top.size

    a.pour_into(b)

    assert len(a) + len(b) == len_a + len_b
    assert len(a) == len_a - shift
    assert len(b) == len_b + shift

    assert b.top.size == b_top_size + shift


def test_pour_single_top_same_space_available():
    a = Beaker(['b', 'o', 'o', 'r'])
    b = Beaker(['b'])

    len_a = len(a)
    len_b = len(b)
    shift = a.top.size
    b_top_size = b.top.size

    a.pour_into(b)

    assert len(a) + len(b) == len_a + len_b
    assert len(a) == len_a - shift
    assert len(b) == len_b + shift

    assert b.top.size == b_top_size + shift


def test_pour_multiple_top_same_space_available():
    a = Beaker(['o', 'o', 'r'])
    b = Beaker(['o', 'r'])

    len_a = len(a)
    len_b = len(b)
    shift = a.top.size
    b_top_size = b.top.size

    a.pour_into(b)

    assert len(a) + len(b) == len_a + len_b
    assert len(a) == len_a - shift
    assert len(b) == len_b + shift

    assert b.top.size == b_top_size + shift
