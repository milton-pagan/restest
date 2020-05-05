from util.lang_def.restest_yacc import Parser


def simple_parse_test():
    parser = Parser().build_parser()

    input_program = """
        (url "localhost:8080") 
        
        (header ["content-type":"application/json", "Accepts":"application/json"]) 
        
        before function("hola", "mundo") (test on "/car" test1:
            define exp 3 + 7 * (5 / 7) + 8 * 40
            get("", id<<3, hola<<36)
            post(id<<3, dimelo<<98)
            put("")
            verify something == something.2.something.something.3
        ) after function("mundo")

        (proc testing[x, y]:
            define exp x * y + 5 * (8 + 7)
            return exp
        )
    """

    return parser.parse(input_program)


"""
if (t[2] is operator and +)
    return self.eval(t[1]) + self.eval(t[3]) 
"""
