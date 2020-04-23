import pytest

from zero_one_sequences.main import swap_count


@pytest.mark.parametrize("seq", ["?", "0", "1"])
def test_single_chars(seq):
    assert swap_count(seq) == 0


@pytest.mark.parametrize("seq, expected", [
    ("??", 1),
    ("???", 6),
    ("?0?", 3),
    ("?1?", 3)
])
def test_question_chars(seq, expected):
    assert swap_count(seq) == expected


@pytest.mark.parametrize("seq, expected", [
    ("1010", 3),
    ("1010?", 8),
    ("1010??", 21),
    ("1010???", 54),
    ("?1010", 8),
    ("?10", 3),
    ("?1", 0),
    ("1?10", 6),
    ("1?1", 1),
    ("1?0", 4),
    ("1010101010", 15),
    ("1010101010?", 35),
    ("10???", 26),
    ("11???", 30),
    ("11?", 2)
])
def test_questions(seq, expected):
    assert swap_count(seq) == expected


@pytest.mark.parametrize("seq, expected", [
    ("00000000000000", 0),
    ("1111111111111111111", 0)
])
def test_no_swaps(seq, expected):
    assert swap_count(seq) == expected
