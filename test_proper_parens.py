from proper_parens import proper_parens


def test_equal():
    text = 'We are (EQUAL)!'
    assert proper_parens(text) == 0


def test_greater_closed():
    text = 'Everyone (is (more) closed) off) here.'
    assert proper_parens(text) == -1


def test_greated_open():
    text = 'The openness) (is (refreshing.'
    assert proper_parens(text) == 1
