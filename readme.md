Python Parser Fun
=================

A simple unreliable parser/tokenizer made in Python in the most
straight-forward way. Probably for didatic ends (who knows?).

Current Usage Example
---------------------

1. Create an `Enum` subtype in which each kind of token has its regex as value:

   ```python
   from enum import Enum
   
   class Tokens(Enum):
       NUMBER = r'\d+'
       IDENTIFIER = r'\w[\w\d]+'
   ```

2. Construct an `pyrser.Tokenizer` with your `Enum`:

   ```python
   from pyrser import Tokenizer

   # ...

   if __name__ == '__main__':
       # ...
       tokenizer = Tokenizer(Tokens)
   ```

3. Feed it with strings and check outputs:

   ```python
       print(tokenizer.tokenize('100'))       # => Tokens.NUMBER
       print(tokenizer.tokenize('something')) # => Tokens.IDENTIFIER
   ```

4. Run and see :)
