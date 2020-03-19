from utils.restest_lexer import Lexer


def test_tokens():

    lexer_wrapper = Lexer()
    lexer = lexer_wrapper.build()

    test_input = '(header hi [CT:JSON, ACC:JSON])  3.14.15 == !=   > <  '

    lexer.input(test_input)

    tokens = []

    while True:
        token = lexer.token()
        if not token:
            break
        tokens.append(token)

    return tokens
