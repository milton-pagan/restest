from util.api.base.base_instruction import BaseInstruction


def verify_test():

    bi = BaseInstruction("First Test", None, "hello", "hey")
    bi.variables = {"x": 30, "y": "2.0", "z": "5"}
    op1 = ("object", ("id", "z"))
    op2 = (
        "math_expression",
        ("factor", 5.2),
        ("operator", "+"),
        (
            "term",
            ("factor", 5),
            ("operator", "*"),
            ("factor", ("term", ("factor", 10), ("operator", "/"), ("factor", 2))),
        ),
    )

    bi2 = BaseInstruction("Second Test", None, "hello", "hey")
    bi2.variables = {"x": 30, "y": "2.0", "z": "5"}
    op12 = ("object", ("id", "z"))
    op22 = (
        "math_expression",
        ("factor", 5.2),
        ("operator", "+"),
        (
            "term",
            ("factor", 5),
            ("operator", "*"),
            ("factor", ("term", ("factor", 10), ("operator", "/"), ("factor", 2))),
        ),
    )

    bi.verify(">=", op12, op22)
    bi.verify("==", op1, op2)
    bi.verify("<=", op12, op22)
    bi.verify(">", op1, op2)
    bi.verify("<", op12, op22)
    bi.verify("!=", op1, op2)
    bi2.verify("<", op1, op2)
    bi2.verify("<=", op12, op22)
    bi2.verify(">=", op1, op2)
    bi2.verify(">=", op1, op2)
    bi2.verify("<=", op12, op22)
    bi2.verify(">=", op1, op2)
    bi2.verify("!=", op1, op2)
