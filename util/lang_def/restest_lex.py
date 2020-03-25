import ply.lex as lex
from ply.lex import TOKEN


class Lexer:
    # Keywords

    reserved = {
        "test": "TEST",
        "on": "ON",
        "for": "FOR",
        "before": "BEFORE",
        "after": "AFTER",
        "url": "URL",
        "proc": "PROC",
        "header": "HEADER",
        "if": "IF",
        "else": "ELSE",
        "def": "DEFINE",
        "verify": "VERIFY",
        "get": "GET",
        "post": "POST",
        "put": "PUT",
        "delete": "DELETE",
        "and": "AND",
        "or": "OR",
        "not": "NOT",
    }
    
    operators = {
        r"\+": "PLUS",
        "-": "MINUS",
        r"\*": "MULT",
        r"/": "DIV",
        "==": "EQ",
        r"\!=": "NEQ",
        ">=": "GEQ",
        "<=": "LEQ",
        ">": "GT",
        "<": "LT",
    }

    # Tokens

    tokens = [
        "IDENTIFIER",
        "OPERATOR",
        "NUMBER",
        "STRING",
        "SEPARATOR",
        "LP",
        "RP",
        "LB",
        "RB",
        "COLON",
        "DOT",
        "COMMA",
        "COMMENT",
        "HEADER_PARAMETERS",
    ] + list(reserved.values())

    # Macros

    letter = r"[a-zA-Z]"
    identifier = letter + r"(\d|" + letter + r"|_|-)*"
    header_params = r"([\w]+:[\w]+,?[\s]*)+"
    operator = r"(\+|-|\*|/|==|!=|>=|<=|>|<)"

    # REGEX
    t_ignore = " \t"
    t_ignore_COMMENT = r"(\#\*[\s\S]*?\*\#)|(\#.*)"

    t_SEPARATOR = r"\n|\\"

    t_RP = r"\)"

    t_LP = r"\("

    t_LB = r"\["

    t_RB = r"\]"

    t_COLON = r":"

    t_DOT = r"\."

    t_COMMA = r","

    t_STRING = r'"([^"\n]|(\\"))*"'

    @TOKEN(header_params)
    def t_HEADER_PARAMETERS(self, t):
        return t

    @TOKEN(identifier)
    def t_IDENTIFIER(self, t):
        t.type = self.reserved.get(t.value, "IDENTIFIER")
        return t

    def t_NUMBER(self, t):
        r"(\+|-)?(\d*\.\d+|\d+)"
        if "." in t.value:
            t.value = float(t.value)
        else:
            t.value = int(t.value)
        return t

    @TOKEN(operators)
    def t_OPERATOR(self, t):
        t.type = self.operators[t.value]

        return t

    # To keep track of line numbers
    def t_newline(self, t):
        r"\n+"
        t.lexer.lineno += len(t.value)

    # Error handler
    def t_error(self, t):
        print("Error on line: %d \n Caused by: %s" % (t.lexer.lineno, t.value[0]))
        t.lexer.skip(1)

    def build(self, **kwargs):
        return lex.lex(module=self, **kwargs)
