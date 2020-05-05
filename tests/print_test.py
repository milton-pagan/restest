from util.lang_def.restest_lex import Lexer


def test_tokens():

    lexer_wrapper = Lexer()
    lexer = lexer_wrapper.build()

    test_input = """
        "{
            'product_name': 'mineral water',
            'product_description': 'bottle',
            'product_price': 0,
            'product_quantity': 100,
            'latitude': 50,
            'longitude': 100.5,
            'category': 'water',
            'category_attributes': {
                'water_exp_date': '2020-05-20',
                'water_volume_ml': 500
            }
        }"
    """

    lexer.input(test_input)

    tokens = []

    while True:
        token = lexer.token()
        if not token:
            break
        tokens.append(token)

    return tokens
