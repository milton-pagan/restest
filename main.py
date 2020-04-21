import sys
from pprint import pprint
from tests.print_test import test_tokens
from tests.print_parser_test import simple_parse_test
from util.api.test import Test
from tests.eval_math_test import eval_math_test
from util.api.base.base_instruction import BaseInstruction
from tests.print_eval_crud_test import test1
from tests.print_access_object import access_object
from tests.verify_test import verify_test

if __name__ == "__main__":
    if "-tl" in sys.argv:
        pprint(test_tokens())

    if "-tp" in sys.argv:
        pprint(simple_parse_test())

    if "-tm" in sys.argv:
        print(eval_math_test())

    if "-toa" in sys.argv:
        access_object()

    if "-tc" in sys.argv:
        test1()
    
    if "-tv" in sys.argv:
        print(verify_test())
