from util.api.base.base_instruction import BaseInstruction


def verify_test():

    bi = BaseInstruction("somthing", None, "hello", "hey")
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

    bi.verify(">=", op1, op2)
    bi.verify("==", op1, op2)
    bi.verify("<=", op1, op2)
    bi.verify(">", op1, op2)
    bi.verify("<", op1, op2)
    bi.verify("!=", op1, op2)
    bi.verify(">=", op1, op2)
    bi.verify(">=", op1, op2)
    bi.verify(">=", op1, op2)
    bi.verify(">=", op1, op2)
    bi.verify(">=", op1, op2)
    bi.verify(">=", op1, op2)
    bi.verify(">=", op1, op2)
