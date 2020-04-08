from util.api.base.base_crud import BaseCrud
from util.api.base.base_instruction import BaseInstruction


class Procedure(BaseInstruction, BaseCrud):
    def __init__(self, name, get_proc, base_url, header):
        super().__init__(name=name, get_proc=get_proc, base_url=base_url, header=header)
        self.seq = []


    def run(self, *kwargs):
        for i in args:
            pass
        for i in self.seq:
            pass

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