from util.lang_def.restest_yacc import Parser


def simple_parse_test():
    parser = Parser().build_parser()

    input_program = """
        (url "localhost:8080") 
        
        (header ["content-type":"application/json", "Accepts":"application/json"]) 
        
        before function("hola", "mundo") (test on "/car" test1:
            define exp 3 + x * (5 / 7) + 8 * 40
        ) after function("mundo")
    """

    return parser.parse(input_program)



"""
if (t[2] is operator and +)
    return self.eval(t[1]) + self.eval(t[3]) 
"""