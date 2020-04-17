from util.api.base.base_crud import BaseCrud
from pprint import pprint


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
        if type(op1) == tuple and type(op2) == tuple:
            if op1[0] == "object" and op2[0] == "object":
                comp_op1 = self.access_object(op1)
                comp_op2 = self.access_object(op2)
                try:
                    if type(comp_op1) == type(comp_op2) == 5:
                        pass

                except TypeError:
                    raise TypeError("Invalid types")

            if op1[0] == "math_expression" and op2[0] == "object":
                comp_op1 = self.eval_math(op1)
                comp_op2 = self.access_object(op2)
                return self.v_calc(comp_op1, operation, comp_op2)

            if op1[0] == "object" and op2[0] == "math_expression":
                comp_op1 = self.access_object(op1)
                comp_op2 = self.eval_math(op2)
                return self.v_calc(comp_op1, operation, comp_op2)

        if type(op1) == tuple:
            if op1[0] == "object":
                return self.v_calc(self.access_object(op1), operation, op2)
            if op1[0] == "math_expression":
                return self.v_calc(self.eval_math(op1), operation, op2)

        if type(op2) == tuple:
            if op2[0] == "object":
                return self.v_calc(op1, operation, self.access_object(op2))
            if op2[0] == "math_expression":
                return self.v_calc(op1, operation, self.eval_math(op2))

        return self.v_calc(op1, operation, op2)

    def v_calc(self, op1, operator, op2):
        if operator == "==":
            return op1 == op2

        if operator == "!=":
            return op1 != op2

        if operator == ">=":
            return op1 >= op2

        if operator == "<=":
            return op1 <= op2

        if operator == ">":
            return op1 > op2

        if operator == "<":
            return op1 < op2

    def eval_math(self, expression):

        if expression[0] == "factor":
            if type(expression[1]) == tuple:
                if expression[1][0] == "object":
                    return self.access_object(e)  # Change to access object
                return self.eval_math(expression[1])
            return expression[1]

        return self.calc(
            self.eval_math(expression[1]),
            expression[2][1],
            self.eval_math(expression[3]),
        )

    def _calc(self, expression1, operator, expression2):
        if operator == "+":
            return expression1 + expression2

        if operator == "-":
            return expression1 - expression2

        if operator == "/":
            return expression1 / expression2

        return expression1 * expression2

    def access_object(self, value: tuple):
        return self._helper_access(value, self.variables)

    def _helper_access(self, value, temp):
        if len(value) == 3:
            return self._helper_access(value[2][1], temp[value[1][1]])
        else:
            return temp[value[1][1]]

    def eval_crud(self, value: tuple):
        if len(value) == 0:
            raise ValueError("Value cannot be empty")

        if len(value) == 1:
            return self.crud[value[0]](body=None).to_dict()

        if len(value) == 3 and type(value[1][1]) == str:
            param_dict = {x[0]: x[1] for x in value[2][1]}
            return self.crud[value[0]](body=value[1][1], **param_dict).to_dict()

        elif len(value) == 3 and type(value[1][1]) == tuple:
            param_dict = {x[0]: x[1] for x in value[2][1]}
            return self.crud[value[0]](
                body=self.access_object(value[1][1]), **param_dict
            ).to_dict()

        elif len(value) == 2 and value[1][0] == "crudbody":
            return self.crud[value[0]](body=value[1][1]).to_dict()

        elif len(value) == 2 and value[1][0] == "crudargs":
            param_dict = {x[0]: x[1] for x in value[1][1]}
            return self.crud[value[0]](body=None, **param_dict).to_dict()

        else:
            return self.crud[value[0]](body=self.access_object(value[1][1])).to_dict()
