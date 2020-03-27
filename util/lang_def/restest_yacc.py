import ply.yacc as yacc
from util.lang_def.restest_lex import Lexer

tokens = Lexer.tokens
lexer = Lexer().build()

class Paser(object):

    def p_test_sequence(self, p):
        """
        test_sequence: url SEPARATOR header SEPARATOR execution test_sequence
                     | url SEPARATOR execution test_sequence
                     | url SEPARATOR header SEPARATOR execution
                     | url SEPARATOR execution
        """
        
        if len(p) == 7:
            p[0] = [p[1], p[3], p[5]] + p[6]
       
        elif len(p) == 5:
            p[0] = [p[1], p[3]] + p[5]

        elif len(p) == 6:
            p[0] = [p[1], p[3], p[5]]
        
        else:
            p[0] = [p[1], p[3]]
            


    def p_url(self, p):
        """
        url : LP URL STRING RP program
        """


    def p_error(self, p):
        print("Syntax error!")


    def build_parser(self):
        parser = yacc.yacc(tabmodule="restest_parser")
        return parser
