from util.api.base.base_crud import BaseCrud
from util.api.base.base_instruction import BaseInstruction


class Procedure(BaseInstruction, BaseCrud):
    def __init__(self, name, get_proc, base_url, header):
        super().__init__(name=name, get_proc=get_proc, base_url=base_url, header=header)
