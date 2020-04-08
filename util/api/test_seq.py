import requests
from util.api.test import Test
from util.api.procedure import Procedure


class TestSequence(object):
    def __init__(self, base_url, initial_header):
        self.procedure_registry = {}
        self.base_url = base_url
        self.initial_header = initial_header

    def register(self, instruction):
        if isinstance(instruction, Test):
            pass
        elif isinstance(instruction, Procedure):
            pass

    def get_proc(self, name="proc"):
        try:
            return self.procedure_registry[name]
        except KeyError:
            raise KeyError(f"procedure {name} not defined")


"""

    temp = Test(...)
            .on(...)
            .define(....)
            .verify()
            .build()

    urls = {}

    test_sequence = TestSequence()

    for i in tests:
        if i[0] == procedure:
            temp = Procedure()
            test_sequence.register(temp)

    test1 = Test()

    test1.define(....)

    test1.verify(....)

    test_sequence.register(test1)
    test_sequence.run()

"""
