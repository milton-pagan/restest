from util.restest_lexer import Lexer

def test_tokens():

    lexer_wrapper = Lexer()
    lexer = lexer_wrapper.build()

    test_input = 'test on and 3.56 a_duro-123'
    
    lexer.input(test_input)

    tokens = []

    while True:
        token = lexer.token()
        if not token:
            break
        tokens.append(token)
    
    return tokens