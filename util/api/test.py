from util.api.base.base_crud import BaseCrud
from util.api.base.base_instruction import BaseInstruction


class Test(BaseCrud, BaseInstruction):
    def __init__(self, name, base_url, get_proc, header):
        super().__init__(name=name, base_url=base_url, get_proc=get_proc, header=header)

    def on(self, str_concat):
        self.url = self.url + str_concat

    def before(self, proc_name, **kwargs):
        self.variables["before_val"] = self.get_proc(proc_name).run(**kwargs)

    def after(self, proc_name, **kwargs):
        self.get_proc(proc_name).run(**kwargs)
