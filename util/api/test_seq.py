import requests
from util.api import *


class TestSequence(object):
    def __init__(self, base_url, initial_header):
        self.procedure_registry = {}
        self.base_url = base_url
        self.initial_header = initial_header

    def register_proc(self, procedure):
        self.procedure_registry[procedure.name] = procedure

    def get_proc(self, name="proc", base_url=None, header=None):
        try:
            proc = self.procedure_registry[name]
            proc.base_url = base_url
            proc.header = header
            return proc
        except KeyError:
            raise KeyError(f"procedure {name} not defined")
