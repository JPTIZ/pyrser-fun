from dataclasses import dataclass
from enum import Enum
from typing import Type
import re


class UnknownToken(Exception):
    pass


@dataclass
class Tokenizer:
    table: Type[Enum]

    def tokenize(self, text: str):
        for token_type in self.table:
            if re.fullmatch(token_type.value, text) is not None:
                return token_type

        raise UnknownToken(f'Unknown token pattern: {text}')
