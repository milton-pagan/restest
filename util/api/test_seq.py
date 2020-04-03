import requests


class TestSequence(object):
    def __init__(self, base_url):
        self.procedure_registry = {}
        self.base_url = base_url

    def register(self, proc):
        pass


"""
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
