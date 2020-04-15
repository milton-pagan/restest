from util.api.base.base_crud import BaseCrud
from util.api.base.base_instruction import BaseInstruction


class Procedure(BaseInstruction):
    def __init__(self, name, get_proc, base_url, header, param_list):
        super().__init__(name=name, get_proc=get_proc, base_url=base_url, header=header)
        self.seq = []
        self.param_list = param_list

    def register_action(self, value: tuple):
        if value[0] == "definition":
            if type(value[2]) == tuple:
                if value[2][0] == "math_expression":
                    self.seq.append(
                        lambda: self.define(value[1][1], self.eval_math(value[2]))
                    )
                elif value[2][0] == "procedure_call":
                    self.seq.append(
                        lambda: self.define(
                            value[1][1], self.get_proc(value[1][1]).run(value[2][1])
                        )
                    )
                else:
                    self.seq.append(lambda: self.define(value[1][1], None))
            else:
                self.seq.append(lambda: self.define(value[1][1], value[2]))

        elif value[0] == "procedure_call":
            self.seq.append(lambda: self.get_proc(value[1][1]).run(value[2][1]))

        elif value[0] == "verify":
            op1 = None
            op2 = None

            if type(value[2]) == tuple:
                if value[2][0] == "math_expression":
                    op1 = self.eval_math(value[2])
                else:
                    op1 = self.access_object(value[2])
            else:
                op1 = value[2]

            if type(value[3] == tuple):
                if value[2][0] == "math_expression":
                    op1 = self.eval_math(value[3])
                else:
                    op1 = self.access_object(value[3])
            else:
                op2 = value[3]

            self.seq.append(lambda: self.verify(value[1][1], op1, op2))

        elif value[0] == "return":
            pass

        else:
            self.seq.append(self.eval_crud(value))

        """
            ('verify',
           ('operator', '=='),
           ('object', ('id', 'something')),
           ('object',
            ('id', 'something'),
            ('ref',
             ('object',
              ('id', 'something'),
              ('ref',
               ('object',
                ('id', 'something'),
                ('ref', ('object', ('id', 'something')))))))))),
        """

    def run(self, *args):
        if len(args) != len(self.param_list):
            raise TypeError(f"Wrong number of arguments in {self.name} call")

        for name, value in zip(self.param_list, args):
            self.define(name, value)
        for i in self.seq:
            i()


"""


(proc add(x, y): 
    define r x+y

    return r
)

test_proc = Procedure(name=add, ....)

test_proc.register_define(tuplo)

register_define(self, name, tuplo):
    if tuplo is math_expression:
        self.seq.append(lambda: self.define(name, self.eval_math(tuplo)))
"""
