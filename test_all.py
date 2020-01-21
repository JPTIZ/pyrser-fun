from enum import Enum
import pytest

from pyrser import Tokenizer


class Tokens(Enum):
    NUMBER = r'\d+'
    IDENTIFIER = r'\w[\w\d]+'


def test_one_digit_number():
    tokenizer = Tokenizer(Tokens)
    assert tokenizer.tokenize('1') == Tokens.NUMBER


def test_multiple_digits_number():
    tokenizer = Tokenizer(Tokens)
    assert tokenizer.tokenize('100') == Tokens.NUMBER


def test_identifiers():
    tokenizer = Tokenizer(Tokens)
    assert tokenizer.tokenize('a100') == Tokens.IDENTIFIER


if __name__ == '__main__':
    pytest.main()
