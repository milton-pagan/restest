import os

from util.lang_def.restest_yacc import Parser
from util.api import *
from util.exceptions.file_type_error import FileTypeError
from core.stdlib import native_functions

class Reader(object):
    def __init__(self):
        self.parser = Parser().build_parser()
        self.test_seq = TestSequence(base_url=None, initial_header=None)
        for proc in native_functions.build_all():
            self.test_seq.register_proc(proc)

    def run(self):
        if not self.parse_tree:
            raise ValueError("No parse tree to read")
        self._helper_run(self.parse_tree)

    def _helper_run(self, tree, parent=None):

        for child in tree:
            if type(child) == tuple:
                if child[0] == "url":
                    self.test_seq.base_url = child[1].strip('"')
                elif child[0] == "header":
                    self.test_seq.initial_header = self.parse_header(child[1])
                elif child[0] == "execution":
                    self._execution_run(child[1])

    def _execution_run(self, execution_itr):

        for child in execution_itr:

            if child[0] == "procedure":
                
                    
                procedure = Procedure(
                    child[1][1], # na
                    self.test_seq.get_proc,# get_proc
                    self.test_seq.base_url,# base url
                    self.test_seq.initial_header,# initial header
                    child[2][1] if child[2][0] == "procedure_parameters" else tuple()
                )

                for action in child[2:]:
                    if "expression" in action:
                        for x in action[1]:
                            procedure.register_action(x)
                    elif "return" in action:
                        procedure.register_action(action)

                self.test_seq.register_proc(procedure)

            elif child[0] == "test":
                test = Test(
                    name=child[1][1],
                    base_url=self.test_seq.base_url,
                    get_proc=self.test_seq.get_proc,
                    header=self.test_seq.initial_header
                )
                for action in child[1:]:
                    test.execute(action)

    def read_file(self, path):
        if not path.endswith(".rsts"):
            try:
                raise FileTypeError(f"Invalid file type: {os.path.splitext(path)}")
            except IndexError:
                raise FileTypeError(f"Invalid file type: No file type")
        with open(path, "r") as file:
            self.parse_tree = self.parser.parse(file.read())
            if self.parse_tree == None:
                exit(1)


    def parse_header(self, header_params):
        header = {}

        for param in header_params:
            header[param[0].strip('"')] = param[1].strip('"')

        return header
