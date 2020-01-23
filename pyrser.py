from dataclasses import dataclass
from enum import Enum
from typing import Type
import re


class UnknownToken(Exception):
    pass


END = object()


@dataclass
class Token:
    type: Enum
    text: str


@dataclass
class Tokenizer:
    table: Type[Enum]

    def tokenize(self, text: str) -> Type[Enum]:
        for token_type in self.table:
            if re.fullmatch(token_type.value, text) is not None:
                return Token(token_type, text)

        raise UnknownToken(f'Unknown token pattern: {text}')
