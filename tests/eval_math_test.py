from util.api.base.base_instruction import BaseInstruction


def eval_math_test():

    input = (
        "math_expression",
        (
            "math_expression",
            ("factor", 3),
            ("operator", "+"),
            (
                "term",
                ("factor", 7),
                ("operator", "*"),
                ("factor", ("term", ("factor", 5), ("operator", "/"), ("factor", 7))),
            ),
        ),
        ("operator", "+"),
        ("term", ("factor", 8), ("operator", "*"), ("factor", 40)),
    )
    return BaseInstruction("somthing", None, "hello", "hey").eval_math(input)

