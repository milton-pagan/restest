class BaseInstruction(object):
    def __init__(self, name, get_proc, **kwargs):
        super().__init__()
        self.name = name
        self.get_proc = get_proc
        self.variables = {}

    def define(self, name, value):
        if type(value) == tuple:
            self.variables[name] = self.eval_math(value)
        else:
            self.variables[name] = value

    def verify(self, operation, op1, op2):
        pass

    def eval_math(self, expression):

        if expression[0] == 'factor':
            if type(expression[1]) == tuple:
                if expression[1][0] == 'object':
                    return self.variables.get(expression[1][0])
                return self.eval_math(self, expression[1])
            return expression[1][0]

        if expression[0] == 'math_expression':
            pass
        
                
        return 0
