from util.lang_def.restest_lex import Lexer


def test_tokens():

    lexer_wrapper = Lexer()
    lexer = lexer_wrapper.build()

    test_input = "(header [\"CT\":\"JSON\", \"SOMETHING\":\"BLAH\", \"SOMETHING\":\"BLAH\"])"

    lexer.input(test_input)

    tokens = []

    while True:
        token = lexer.token()
        if not token:
            break
        tokens.append(token)

    return tokens
