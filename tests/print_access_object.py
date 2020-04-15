import sys
from util.api.base.base_instruction import BaseInstruction
from tests.print_eval_crud_test import test1


def access_object():
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

