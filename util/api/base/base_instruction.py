class BaseInstruction(object):
    def __init__(self, name, get_proc, **kwargs):
        super().__init__()
        self.name = name
        self.get_proc = get_proc
        self.variables = {}

    def define(self, name, value):
        if type(value) == tuple:
            self.variables = self.eval_math(value)
        else:
            self.variables[name] = value

    def verify(self, operation, op1, op2):
        pass

    def eval_math(self, expression):
        pass
