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
        "define": "DEFINE",
        "verify": "VERIFY",
        "get": "GET",
        "post": "POST",
        "put": "PUT",
        "delete": "DELETE",
        "and": "AND",
        "or": "OR",
        "not": "NOT",
        "return": "RETURN",
    }

    operators = {
        "+": "PLUS",
        "-": "MINUS",
        "*": "MULT",
        "/": "DIV",
        "==": "EQ",
        "!=": "NEQ",
        ">=": "GEQ",
        "<=": "LEQ",
        ">": "GT",
        "<": "LT",
    }

    # Tokens

    tokens = (
        [
            "IDENTIFIER",
            "OPERATOR",
            "INTEGER",
            "FLOAT",
            "STRING",
            "SEPARATOR",
            "LP",
            "RP",
            "LB",
            "RB",
            "LC",
            "RC",
            "COLON",
            "DOT",
            "COMMA",
            "COMMENT",
        ]
        + list(reserved.values())
        + list(operators.values())
    )

    # Macros

    letter = r"[a-zA-Z]"
    identifier = letter + r"(\d|" + letter + r"|_|-)*"
    operator = r"(\+|-|\*|/|==|!=|>=|<=|>|<)"

    # REGEX
    t_ignore = " |\t|\r"
    t_ignore_COMMENT = r"(\#\*[\s\S]*?\*\#)|(\#.*)"

    t_RP = r"\)"

    t_LP = r"\("

    t_LB = r"\["

    t_RB = r"\]"

    t_LC = r"{"

    t_RC = r"}"

    t_COLON = r":"

    t_DOT = r"\."

    t_COMMA = r","

    t_STRING = r'"([^"\n]|(\\"))*"'

    @TOKEN(identifier)
    def t_IDENTIFIER(self, t):
        t.type = self.reserved.get(t.value, "IDENTIFIER")
        return t

    def t_FLOAT(self, t):
        r"(\+|-)?(\d+\.\d+)"

        t.value = float(t.value)
        return t

    def t_INTEGER(self, t):
        r"(\+|-)?(\d+)"
        t.value = int(t.value)
        return t

    @TOKEN(operator)
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
