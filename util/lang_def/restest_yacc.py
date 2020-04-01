import ply.yacc as yacc
from util.lang_def.restest_lex import Lexer


class Parser(object):

    tokens = Lexer.tokens
    lexer = Lexer().build()

    def p_test_sequence(self, p):
        """
        test_sequence : url  header  execution test_sequence
                      | url  execution test_sequence
                      | url  header  execution
                      | url  execution
        """

        # if len(p) == 7:
        #     p[0] = (p[1], p[3], ("execution", p[5])) + p[6]

        # elif len(p) == 5:
        #     p[0] = (p[1], ("execution", p[3])) + p[5]

        # elif len(p) == 6:
        #     p[0] = (p[1], p[3], ("execution", p[5]))

        # else:
        #     p[0] = (p[1], ("execution", p[3]))
        pass

    def p_url(self, p):
        """
        url : LP URL STRING RP
        """
        # p[0] = ("url", p[3])
        pass

    def p_header(self, p):
        """
        header : LP HEADER LB header_parameters RB RP
        """
        # p[0] = ("header", p[4])
        pass

    def p_header_parameters(self, p):
        """
        header_parameters : STRING COLON STRING
                          | STRING COLON STRING COMMA header_parameters
        """
        # if len(p) == 4:
        #     p[0] = tuple((p[1], p[3]))
        # else:
        #     p[0] = tuple((p[1], p[3])) + p[5]
        pass

    def p_execution(self, p):
        """
           execution : test
                     | procedure
                     | test  execution
                     | procedure  execution
        """

        # if len(p) == 2:
        #     p[0] = tuple(p[1])
        # else:
        #     p[0] = p[1] + p[3]
        pass

    ### TEST ###

    # ('test', ('id', name), ('before', ...), ('on', '...'), ('body', ...), ('after', ...))
    def p_test(self, p):
        """
        test :   before LP TEST IDENTIFIER COLON  expression RP after
             |   before LP TEST IDENTIFIER COLON  expression RP
             |   LP TEST IDENTIFIER COLON  expression RP after
             |   before LP TEST ON STRING IDENTIFIER COLON  expression RP after
             |   before LP TEST ON STRING IDENTIFIER COLON  expression RP
             |   LP TEST ON STRING IDENTIFIER COLON  expression RP after
             |   LP TEST IDENTIFIER COLON  expression RP
             |   LP TEST ON STRING IDENTIFIER COLON  expression RP
        """
        # if len(p) == 10 and type(p[1]) == tuple:
        #     p[0] = ("test", ("id", p[4]), p[1], ("expression", p[7]), p[9])
        # elif len(p) == 9 and type(p[1]) == tuple:
        #     p[0] = ("test", ("id".p[4]), p[1], ("expression", p[7]))
        # elif len(p) == 9:
        #     p[0] = ("test", ("id", p[3]), ("expression", p[6]))
        # elif len(p) == 12:
        #     p[0] = (
        #         "test",
        #         ("id", p[6]),
        #         p[1],
        #         ("on", p[5]),
        #         ("expression", p[9]),
        #         p[11],
        #     )
        # elif len(p) == 11 and type(p[1]) == tuple:
        #     p[0] = ("test", ("id", p[6]), p[1], ("on", p[5]), ("expression", p[9]))
        # elif len(p) == 11:
        #     p[0] = ("test", ("id", p[5]), ("on", p[4]), ("expression", p[8]), p[10])
        pass

    def p_before(self, p):
        """
        before : BEFORE procedure_call 
        """

        # p[0] = ("before", p[2])

    def p_after(self, p):
        """
        after : AFTER procedure_call
        """

        # p[0] = ("after", p[2])

    ### PROCEDURE ###

    def p_procedure(self, p):
        """
        procedure : LP PROC IDENTIFIER LB procedure_parameters RB COLON  expression RP
        """
        # p[0] = (
        #     "procedure",
        #     ("id", p[3]),
        #     ("procedure_parameters", p[5]),
        #     ("expression", p[9]),
        # )

    def p_procedure_parameters(self, p):
        """
        procedure_parameters :   IDENTIFIER
                             |   IDENTIFIER COMMA procedure_parameters
        """

        # if len(p) == 2:
        #     p[0] = tuple(p[1])
        # else:
        #     p[0] = tuple(p[1]) + p[3]

    def p_procedure_call(self, p):
        """
        procedure_call :     IDENTIFIER LP parameters RP
                        |   IDENTIFIER LP RP
        """

        # if len(p) == 5:
        #     p[0] = ("procedure_call", ("id", p[1]), ("parameters", p[4]))
        # else:
        #     p[0] = ("procedure_call", ("id", p[1]))

    def p_parameters(self, p):
        """
        parameters  :   STRING
                    |   NUMBER
                    |   STRING COMMA parameters
                    |   NUMBER COMMA parameters
        """

        # if len(p) == 2:
        #     p[0] = tuple(p[1])
        # else:
        #     p[0] = tuple(p[1]) + p[3]

    ### EXPRESSION ###

    def p_expression(self, p):
        """
        expression  :  line
                    |  line  expression
        """
        # if len(p) == 2:
        #     p[0] = tuple(p[1])
        # else:
        #     p[0] = (p[1], p[3])

    def p_line(self, p):
        """
        line :   instruction
             |   definition
        """
        # p[0] = p[1]

    def p_instruction(self, p):
        """
        instruction :   procedure_call
                    |   verify
                    |   crud
        """

        # p[0] = ("instruction", p[1])

    def p_definition(self, p):
        """
        definition  :   DEFINE IDENTIFIER STRING
                    |   DEFINE IDENTIFIER NUMBER
                    |   DEFINE IDENTIFIER IDENTIFIER
                    |   DEFINE IDENTIFIER procedure_call
                    |   DEFINE IDENTIFIER crud
        """

        # p[0] = ("definition", ("id", p[2]), p[3])

    def p_verify(self, p):
        """
        verify  : VERIFY object EQ object
                | VERIFY math_expression EQ object
                | VERIFY object EQ math_expression
                | VERIFY object EQ STRING
                | VERIFY STRING EQ object
                | VERIFY math_expression NEQ object
                | VERIFY object NEQ math_expression 
                | VERIFY object NEQ STRING
                | VERIFY STRING NEQ object
                | VERIFY object NEQ object
                | VERIFY math_expression LT object
                | VERIFY object LT math_expression
                | VERIFY object LT STRING
                | VERIFY STRING LT object
                | VERIFY math_expression GT object
                | VERIFY object GT math_expression
                | VERIFY object GT STRING
                | VERIFY STRING GT object
                | VERIFY math_expression GEQ object
                | VERIFY object GEQ math_expression
                | VERIFY object GEQ STRING
                | VERIFY STRING GEQ object
                | VERIFY math_expression LEQ object
                | VERIFY object LEQ math_expression
                | VERIFY object LEQ STRING
                | VERIFY STRING LEQ object
        """
        pass

    def p_object(self, p):
        """
        object : IDENTIFIER
               | IDENTIFIER DOT object
        """
        pass

    def p_math_expression(self, p):
        """
        math_expression : math_expression PLUS math_term
                       | math_expression MINUS math_term
                       | math_term
        """
        pass

    def p_math_term(self, p):
        """
        math_term : math_term MULT math_factor
                 | math_term DIV math_factor
                 | math_factor
        """
        pass

    def p_math_factor(self, p):
        """
        math_factor : NUMBER
                   | LP math_expression RP
        """
        pass

    def p_crud(self, p):
        """
        crud : get
             | post
             | put
             | delete
        """
        pass

    def p_get(self, p):
        """
        get : GET LP RP
            | GET LP crudbody RP
            | GET LP crudbody COMMA crudargs RP
            | GET LP crudargs RP
        """
        pass

    def p_post(self, p):
        """
        post : POST LP RP
            | POST LP crudbody RP
            | POST LP crudbody COMMA crudargs RP
            | POST LP crudargs RP
        """
        pass

    def p_put(self, p):
        """
        put : PUT LP RP
            | PUT LP crudbody RP
            | PUT LP crudbody COMMA crudargs RP
            | PUT LP crudargs RP
        """
        pass

    def p_delete(self, p):
        """
        delete : DELETE LP RP
            | DELETE LP crudbody RP
            | DELETE LP crudbody COMMA crudargs RP
            | DELETE LP crudargs RP
        """
        pass

    def p_crudbody(self, p):
        """
        crudbody : object
                 | STRING
        """
        pass

    def p_crudargs(self, p):
        """
        crudargs : crudargs COMMA crudargs
                 | IDENTIFIER LT LT object
                 | IDENTIFIER LT LT STRING
                 | IDENTIFIER LT LT NUMBER
        """
        pass

    def p_error(self, p):
        print("Syntax error at token ", p, " line:", p.lexer.lineno)

    def build_parser(self):
        parser = yacc.yacc(tabmodule="restest_parser", module=self)
        return parser
