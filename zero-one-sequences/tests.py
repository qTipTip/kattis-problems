import pytest

from main import swap_count


@pytest.mark.parametrize("seq", [b"?", b"0", b"1"])
def test_single_chars(seq):
    assert swap_count(seq) == 0


@pytest.mark.parametrize("seq, expected", [
    (b"??", 1),
    (b"???", 6),
    (b"?0?", 3),
    (b"?1?", 3)
])
def test_question_chars(seq, expected):
    assert swap_count(seq) == expected


@pytest.mark.parametrize("seq, expected", [
    (b"1010", 3),
    (b"1010?", 8),
    (b"1010??", 21),
    (b"1010???", 54),
    (b"?1010", 8),
    (b"?10", 3),
    (b"?1", 0),
    (b"1?10", 6),
    (b"1?1", 1),
    (b"1?0", 4),
    (b"1010101010", 15),
    (b"1010101010?", 35),
    (b"10???", 26),
    (b"11???", 30),
    (b"11?", 2)
])
def test_questions(seq, expected):
    assert swap_count(seq) == expected


@pytest.mark.parametrize("seq, expected", [
    (b"00000000000000", 0),
    (b"1111111111111111111", 0)
])
def test_no_swaps(seq, expected):
    assert swap_count(seq) == expected
