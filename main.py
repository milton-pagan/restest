import sys
from core.reader import Reader

if __name__ == "__main__":
    reader = Reader()

    # if len(sys.argv) != 2:
    #     print("Invalid arguments!")
    #     exit(-1)

    path = "/home/milpa/college/courses/prog_lang/restest/tests/resources/test_program.rsts"

    reader.read_file(path)
    reader.run()
