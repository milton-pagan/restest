from util.api.base.base_crud import BaseCrud
from util.api.base.base_instruction import BaseInstruction


class Procedure(BaseInstruction):
    def __init__(self, name, get_proc, base_url, header, *param_list):
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
                            value[1][1],
                            self.get_proc(value[2][1][1], self.base_url).run(
                                value[2][1]
                            ),
                        )
                    )
                else:  # CRUD
                    self.seq.append(
                        lambda: self.define(value[1][1], self.eval_crud(value[2]))
                    )
            else:  # Primitive type
                self.seq.append(lambda: self.define(value[1][1], value[2]))

        elif value[0] == "procedure_call":
            self.seq.append(
                lambda: self.get_proc(value[1][1], self.base_url).run(*value[2][1])
            )

        elif value[0] == "verify":
            self.seq.append(lambda: self.verify(value[1][1], value[2], value[3]))

        elif value[0] == "return":
            self.seq.append(lambda: self.ret(value[1]))

        else:
            self.seq.append(lambda: self.eval_crud(value))

    def run(self, *args):
        if len(args) != len(self.param_list):
            raise TypeError(f"Wrong number of arguments in {self.name} call")
        for name, value in zip(self.param_list, args):
            self.define(name, value)
        for i in self.seq:
            temp = i()
            if type(temp) == tuple:
                return temp[1]

    def ret(self, value):
        if type(value) == "tuple":
            if value[0] == "object":
                return ("return", self.access_object(value))
            elif value[0] == "math_expression":
                return ("return", self.eval_math(value))
            elif value[0] == "procedure_call":
                return ("return", self.get_proc(value[1][1], self.base_url))
            else:
                return ("return", self.eval_crud(value))
        return ("return", value)
