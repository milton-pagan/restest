import sys
from pprint import pprint
from tests.print_test import test_tokens
from tests.print_parser_test import simple_parse_test
from util.api.test import Test
from tests.eval_math_test import eval_math_test

if __name__ == "__main__":
    if "-tl" in sys.argv:
        pprint(test_tokens())
    if "-tp" in sys.argv:
        pprint(simple_parse_test())
    if "-tm" in sys.argv:
        print(eval_math_test())
