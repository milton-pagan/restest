from util.api.base.base_crud import BaseCrud
from util.api.base.base_instruction import BaseInstruction


class Test(BaseInstruction):
    def __init__(self, name, base_url, get_proc, header):
        super().__init__(name=name, base_url=base_url, get_proc=get_proc, header=header)

    def on(self, str_concat):
        self.base_url = self.base_url + str_concat

    def before(self, proc_name, *args):
        self.variables["before_val"] = self.get_proc(
            proc_name, self.base_url, header=self.header
        ).run(*args)

    def after(self, proc_name, *args):
        self.get_proc(proc_name, self.base_url, header=self.header).run(*args)

    def execute(self, action):

        if action[0] == "id":
            self.name == action[1]

        elif action[0] == "before":
            if len(action[1]) == 2:
                self.before(action[1][1][1])
            elif len(action[1]) == 3:
                self.before(
                    action[1][1][1],
                    *[
                        self.access_object(x) if type(x) == tuple else x
                        for x in action[1][2][1]
                    ]
                )

        elif action[0] == "after":
            if len(action[1]) == 2:
                self.after(action[1][1][1])
            elif len(action[1]) == 3:
                self.after(
                    action[1][1][1],
                    *[
                        self.access_object(x) if type(x) == tuple else x
                        for x in action[1][2][1]
                    ]
                )

        elif action[0] == "on":
            self.on(action[1].strip('"'))

        elif action[0] == "expression":
            self._execute_expression(action[1])

    def _execute_expression(self, expression):
        for line in expression:
            if type(line[0]) == tuple:
                line = line[0]

            if line[0] == "instruction":
                self._execute_instruction(line[1])
            elif line[0] == "definition":
                self._execute_definition(line[1][1], line[2])

    def _execute_instruction(self, instruction):
        if instruction[0] == "verify":
            self.verify(instruction[1][1], instruction[2], instruction[3])
        elif instruction[0] == "procedure_call":
            if len(instruction) == 2:
                self.get_proc(instruction[1][1]).run()
            elif len(instruction) == 3:
                self.get_proc(
                    instruction[1][1]
                ).run(*[
                        self.access_object(x) if type(x) == tuple else x
                        for x in instruction[2][1]
                    ])

        else:  # CRUD
            self.eval_crud(instruction)

    def _execute_definition(self, name, value):
        if type(value) == tuple:

            if value[0] == "math_expression":
                self.define(name, self.eval_math(value))

            elif value[0] == "procedure_call":
                if len(value) == 2:
                    self.define(name, self.get_proc(value[1][1]).run())
                elif len(value) == 3:
                    self.define(name, self.get_proc(
                        value[1][1]
                    ).run(*[
                            self.access_object(x) if type(x) == tuple else x
                            for x in value[2][1]
                        ]))          

            elif value[0] == "object":
                self.define(name, self.access_object(value))

            elif value[0] == "dictionary":
                self.define(name, self.parse_dictionary(value))

            else:  # CRUD
                self.define(name, self.eval_crud(value))
        else:
            if type(value) == str:
                self.define(name, value.strip('"'))
            else:
                self.define(name, value)
