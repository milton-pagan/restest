from util.lang_def.restest_lex import Lexer


def test_tokens():

    lexer_wrapper = Lexer()
    lexer = lexer_wrapper.build()

    test_input = 'something.2.something.something.3'

    lexer.input(test_input)

    tokens = []

    while True:
        token = lexer.token()
        if not token:
            break
        tokens.append(token)

    return tokens
