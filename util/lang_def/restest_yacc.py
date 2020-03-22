import ply.yacc as yacc
from util.lang_def.restest_lexer import Lexer

tokens = Lexer.tokens
lexer = Lexer().build()


def p_url(p):
    """
    url : LP URL STRING RP program
    """
    p[0] = [{"url": p[3]}]

    p[0] += p[5]


def p_program(p):
    """
    program: line
           | line program
    """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1]
        p[1].append(p[2])


def p_line(p):
    """
    line: instruction
        | definition
    """
    p[0] = p[1]


def p_instruction(p):
    """
    instruction: test
               | header
               | before
               | after
               | process
               | verify
               | crud
    """
    p[0] = p[1]


# TODO: FINISH
def p_header(p):
    """
    header: LP HEADER IDENTIFIER LB HEADER_PARAMETERS RB
    """


def p_error(p):
    print("Syntax error!")


def build_parser():
    parser = yacc.yacc(tabmodule="restest_parser")
    return parser
