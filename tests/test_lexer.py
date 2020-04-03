import unittest
import re
from pprint import pprint
from util.lang_def.restest_lex import Lexer


class TestLexer(unittest.TestCase):
    def setUp(self):
        LexerWrapper = Lexer()
        self.lexer = LexerWrapper.build()

    def get_span(self, pattern, target):
        match = re.match(pattern, target)
        if match:
            return match.span()
        return None

    def get_token_list(self, test_input):

        lexer = self.lexer

        lexer.input(test_input)

        tokens = []

        while True:
            token = lexer.token()
            if not token:
                break
            tokens.append(token)

        return tokens

    def test_identifier_lexer(self):

        test_input = ' testing t3 x3 x123 "x123" '

        tokens = [x for x in self.get_token_list(test_input) if x.type == "IDENTIFIER"]

        # testing t3 x3 x123
        self.assertEqual(len(tokens), 4)

    # Test operators
    def test_operators_lexer(self):

        test_input = "or and == != > < >= <= not 32 dimelo 12345 x3"

        tokens = [x for x in self.get_token_list(test_input) if x.type == "OPERATOR"]

        # ==, !=,<=, >, <, >=
        self.assertEqual(len(tokens), 6)

    def test_separator_lexer(self):

        test_input = """
            define x3 76 \r
            x3 == \ \n
                5
        """
        tokens = [x for x in self.get_token_list(test_input) if x.type == "SEPARATOR"]
        # \ \n
        self.assertEqual(len(tokens), 3)

    def test_string_lexer(self):

        test_input = ' "Hola" "" " " x3 123 5432 dimelo "Testing 123"  '

        tokens = [x for x in self.get_token_list(test_input) if x.type == "STRING"]

        # "Hola" "" " " "Testing 123"
        self.assertEqual(len(tokens), 4)

    def test_number_lexer(self):

        test_input = ' 3.24 123456789.12345667  "3.56" dimelo 3.14.15 '

        tokens = [x for x in self.get_token_list(test_input) if x.type == "NUMBER"]

        # 3.24  123456789.12345667 3.14 0.15
        self.assertEqual(len(tokens), 4)

    def test_reserved_lexer(self):

        test_input = ' define url x3 43 567 "header url" define url '

        tokens = [
            x
            for x in self.get_token_list(test_input)
            if x.type == "DEFINE" or x.type == "URL"
        ]

        self.assertEqual(len(tokens), 4)

    def test_tokens(self):

        test_input = "(header hi [CT:JSON, ACC:JSON])"

        tokens = self.get_token_list(test_input)

        # all tokens except whitespace
        self.assertEqual(len(tokens), 13)
