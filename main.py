import sys
from pprint import pprint
from tests.print_test import test_tokens
from tests.print_parser_test import simple_parse_test
from util.api.test import Test
from tests.eval_math_test import eval_math_test
from util.api.base.base_instruction import BaseInstruction
from tests.print_eval_crud_test import test1

if __name__ == "__main__":
    test1()
    if "-tl" in sys.argv:
        pprint(test_tokens())
    if "-tp" in sys.argv:
        pprint(simple_parse_test())
    if "-tm" in sys.argv:
        print(eval_math_test())

    if "-toa" in sys.argv:
        variables = {
            "something0": {
                "something1": {"something2": {"something3": "Holaaaa Mundooo"}}
            }
        }

        base_instr = BaseInstruction("name", None, "url", "header")
        base_instr.variables = variables

        print(base_instr.access_object(("object", ("id", "something0"))))
        print(
            base_instr.access_object(
                (
                    "object",
                    ("id", "something0"),
                    (
                        "ref",
                        (
                            "object",
                            ("id", "something1"),
                            (
                                "ref",
                                (
                                    "object",
                                    ("id", "something2"),
                                    ("ref", ("object", ("", "something3"))),
                                ),
                            ),
                        ),
                    ),
                )
            )
        )

    if "-tc" in sys.argv:
        pass
