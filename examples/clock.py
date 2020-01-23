from dataclasses import dataclass
from enum import Enum

import pytest

from pyrser import Tokenizer


@dataclass(frozen=True)
class Time:
    hour: int
    minute: int


class UnexpectedToken(Exception):
    pass


class Tokens(Enum):
    NUMBER = r'\d+'
    HOUR = r'[Hh]'
    MINUTE = r'[Mm]'
    SEPARATOR = r':'


def parse(text: str):
    tokenizer = Tokenizer(Tokens)

    parts = iter(text.split())

    token = tokenizer.tokenize(next(parts))
    if token.type == Tokens.NUMBER:
        hour = int(token.text)
    else:
        raise UnexpectedToken(token.type)

    token = tokenizer.tokenize(next(parts))
    if token.type not in (Tokens.HOUR, Tokens.SEPARATOR):
        raise UnexpectedToken(token.type)

    token = tokenizer.tokenize(next(parts))
    if token.type == Tokens.NUMBER:
        minute = int(token.text)
    else:
        raise UnexpectedToken(token.type)

    try:
        token = tokenizer.tokenize(next(parts))
        if token.type != Tokens.MINUTE:
            raise UnexpectedToken(token.type)
    except StopIteration:
        pass

    return Time(hour, minute)


def test_simple_time():
    assert parse('17 h 45') == Time(17, 45)


def test_simple_time_with_sep():
    assert parse('17 : 45') == Time(17, 45)


def test_simple_time_with_min():
    assert parse('17 h 45 m') == Time(17, 45)


def test_simple_time_uppercase():
    assert parse('17 H 45') == Time(17, 45)


def test_simple_time_with_min_uppercase():
    assert parse('17 H 45 M') == Time(17, 45)


if __name__ == '__main__':
    pytest.main()
