from util.lang_def.restest_yacc import Parser


def simple_parse_test():
    parser = Parser().build_parser()

    input_program = """
        (url "localhost:8080") 
        
        (header ["content-type":"application/json", "Accepts":"application/json"]) 
        
        before function("hola", "mundo") (test on "/car" test1:
            define l1 "hole"
            verify l1 == "hola"
        ) after function("mundo")
    """

    return parser.parse(input_program)
