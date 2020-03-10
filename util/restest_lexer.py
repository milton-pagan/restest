import ply.lex as lex


class Lexer:

    reserved = {
        'test':'TEST',
        'on':'ON',
        'for':'FOR',
        'before':'BEFORE',
        'url':'URL',
        'proc':'PROC',
        'header':'HEADER',
        'if':'IF',
        'else':'ELSE',
        'define':'DEFINE',
        'verify':'VERIFY',
        'get':'GET',
        'post':'POST',
        'put':'PUT',
        'delete':'DELETE'
    }


    # Tokens

    tokens = ['IDENTIFIER', 'OPERATOR', 'NUMBER', 'STRING', 'FLOAT'
        ,'SEPARATOR', 'LP', 'RP', 'COLON', 'DOT'] + list(reserved.values())

    # Macros

    letter = r'[a-zA-Z]'


    # REGEX 
    t_ignore = r' \t'

    t_OPERATOR = r'or|and|not|==|!='

    t_SEPARATOR = r'\n|\\'

    t_RP = r'\)'

    t_LP = r'\('

    t_COLON = r':'

    t_DOT = r'\.'

    t_STRING = r'"([^"\n]|[\\"])*"'

    def t_IDENTIFIER(self): 
        self.letter + r'(\d|' + self.letter + r'|_|-)*'
        return self.letter + r'(\d|' + self.letter + r'|_|-)*'            

    def t_NUMBER(self, t):
        r'(\+|-)?(\d*\.\d+|\d+)'
        if '.' in t.value:
            t.value = float(t.value)
        else:
            t.value = int(t.value)
        return t
    
    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
        return self.lexer

    