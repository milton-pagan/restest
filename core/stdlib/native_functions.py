from util.api import Procedure


def build_all():
    return [build_print(), build_length()]


# name, get_proc, base_url, header, *param_list
def build_print():
    print_proc = Procedure("print", None, None, None, "askdhlhqpurhfp3h4p9234")
    print_proc.seq.append(lambda: print(print_proc.variables[print_proc.param_list[0]]))
    return print_proc


def build_length():
    length_proc = Procedure("len", None, None, None, "askdhlhqpurh")
    length_proc.seq.append(
        lambda: length_proc.ret(len(length_proc.variables[length_proc.param_list[0]]))
    )
    return length_proc
