from util.api.base.base_instruction import BaseInstruction

def verify_test():

    bi = BaseInstruction("somthing", None, "hello", "hey")
    bi.variables =  {
                    "x": 5,
                    "y":"2.0",
                    "z": "5"
                    }
    op1 =   ("object",("id", "y"))  
    op2 = ("object",("id","z"))

    return BaseInstruction("somthing", None, "hello", "hey").verify("==", op1, op2)