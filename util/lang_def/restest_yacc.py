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
            p[0] = (p[1], p[3], ("execution", p[5])) + p[6]

        elif len(p) == 5:
            p[0] = (p[1], ("execution", p[3])) + p[5]

        elif len(p) == 6:
            p[0] = (p[1], p[3], ("execution", p[5]))

        else:
            p[0] = (p[1], ("execution", p[3]))

    def p_url(self, p):
        """
        url : LP URL STRING RP
        """
        p[0] = ("url", p[3])

    def p_header(self, p):
        """
        header: LP HEADER LB header_parameters RB RP
        """
        p[0] = ("header", p[4])

    def p_header_parameters(self, p):
        """
        header_parameters: STRING COLON STRING
                         | STRING COLON STRING COMMA header_parameters
        """
        if len(p) == 4:
            p[0] = tuple((p[1], p[3]))
        else:
            p[0] = tuple((p[1], p[3])) + p[5]

    def p_execution(self, p):
        """
           execution: test
                    | procedure
                    | test SEPARATOR execution
                    | procedure SEPARATOR execution
        """

        if len(p) == 2:
            p[0] = tuple(p[1])
        else:
            p[0] = p[1] + p[3]

    ### TEST ###

    # ('test', ('id', name), ('before', ...), ('on', '...'), ('body', ...), ('after', ...))
    def p_test(self, p):
        """
        test:   before LP TEST IDENTIFIER COLON SEPARATOR expression RP after
            |   before LP TEST IDENTIFIER COLON SEPARATOR expression RP
            |   LP TEST IDENTIFIER COLON SEPARATOR expression RP after
            |   before LP TEST ON STRING IDENTIFIER COLON SEPARATOR expression RP after
            |   before LP TEST ON STRING IDENTIFIER COLON SEPARATOR expression RP
            |   LP TEST ON STRING IDENTIFIER COLON SEPARATOR expression RP after
        """
        if len(p) == 10 and type(p[1]) == tuple:
            p[0] = ("test", ("id", p[4]), p[1], ("expression", p[7]), p[9])
        elif len(p) == 9 and type(p[1]) == tuple:
            p[0] = ("test", ("id".p[4]), p[1], ("expression", p[7]))
        elif len(p) == 9:
            p[0] = ("test", ("id", p[3]), ("expression", p[6]))
        elif len(p) == 12:
            p[0] = (
                "test",
                ("id", p[6]),
                p[1],
                ("on", p[5]),
                ("expression", p[9]),
                p[11],
            )
        elif len(p) == 11 and type(p[1]) == tuple:
            p[0] = ("test", ("id", p[6]), p[1], ("on", p[5]), ("expression", p[9]))
        elif len(p) == 11:
            p[0] = ("test", ("id", p[5]), ("on", p[4]), ("expression", p[8]), p[10])

    def p_before(self, p):
        """
        before: BEFORE procedure_call 
        """

    def p_after(self, p):
        """
        after: AFTER procedure_call
        """

    ### PROCEDURE ###

    def p_procedure(self, p):
        """
        procedure: LP PROC IDENTIFIER LB procedure_parameters RB COLON SEPARATOR expression RP
        """
        p[0] = (
            "procedure",
            ("id", p[3]),
            ("procedure_parameters", p[5]),
            ("expression", p[9]),
        )

    def p_procedure_parameters(self, p):
        """
        procedure_parameters:   IDENTIFIER
                            |   IDENTIFIER COMMA procedure_parameters
        """

        if len(p) == 2:
            p[0] = tuple(p[1])
        else:
            p[0] = tuple(p[1]) + p[3]

    def p_procedure_call(self, p):
        """
        procedure_call:     IDENTIFIER LP parameters RP
                        |   IDENTIFIER LP RP
        """

        if len(p) == 5:
            p[0] = ("procedure_call", ("id", p[1]), ("parameters", p[4]))
        else:
            p[0] = ("procedure_call", ("id", p[1]))

    def p_parameters(self, p):
        """
        parameters:     STRING
                    |   NUMBER
                    |   STRING COMMA parameters
                    |   NUMBER COMMA parameters
        """

        if len(p) == 2:
            p[0] = tuple(p[1])
        else:
            p[0] = tuple(p[1]) + p[3]

    ### EXPRESSION ###

    def p_expression(self, p):
        """
        expression:  line
                  |  line SEPARATOR expression
        """
        pass

    def p_line(self, p):
        """
        line:   instruction
            |   definition
        """
        pass

    def p_instruction(self, p):
        """
        instruction:    procedure_call
                    |   verify
                    |   crud
        """
        pass

    def p_definition(self, p):
        """
        definition:     DEFINE IDENTIFIER STRING
                    |   DEFINE IDENTIFIER NUMBER
                    |   DEFINE IDENTIFIER IDENTIFIER
                    |   DEFINE IDENTIFIER procedure_call
                    |   DEFINE IDENTIFIER crud
        """
        pass

    def p_verify(self, p):
        """
        verify:   VERIFY object EQ object
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

    def p_error(self, p):
        print("Syntax error!")

    def build_parser(self):
        parser = yacc.yacc(tabmodule="restest_parser")
        return parser
        print("Syntax error!")
