from util.api.base.base_crud import BaseCrud


class BaseInstruction(BaseCrud):
    def __init__(self, name, get_proc, base_url, header):
        super().__init__(base_url, header)
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

        if expression[0] == "factor":
            if type(expression[1]) == tuple:
                if expression[1][0] == "object":
                    return self.variables.get(expression[1][0])
                return self.eval_math(expression[1])
            return expression[1]

        return self.calc(
            self.eval_math(expression[1]),
            expression[2][1],
            self.eval_math(expression[3]),
        )

    def calc(self, expression1, operator, expression2):
        if operator == "+":
            return expression1 + expression2

        if operator == "-":
            return expression1 - expression2

        if operator == "/":
            return expression1 / expression2

        return expression1 * expression2

    def access_object(self, value: tuple):
        temp = self.variables[value[1][1]]

    def eval_crud(self, value: tuple):
        if len(value) == 0:
            raise ValueError("Value cannot be empty")

        if len(value) == 1:
            return lambda: self.crud[value[0]](body=None).toDict()

        if len(value) == 3 and type(value[1][1]) == str:
            param_dict = {x[0]: x[1] for x in value[2][1]}
            return lambda: self.crud[value[0]](body=value[1][1], **param_dict).toDict()

        elif len(value) == 3 and type(value[1][1]) == tuple:
            param_dict = {x[0]: x[1] for x in value[2][1]}
            return lambda: self.crud[value[0]](
                body=self.access_object(value[1][1]), **param_dict
            ).toDict()

        elif len(value) == 2 and value[1][0] == "crudargs":
            param_dict = {x[0]: x[1] for x in value[2][1]}
            return lambda: self.crud[value[0]](body=None, **param_dict).toDict()

        else:
            return lambda: self.crud[value[0]](
                body=self.access_object(value[1][1])
            ).toDict()
