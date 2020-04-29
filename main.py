import sys
from core.reader import Reader
from tests.verify_test import verify_test

if __name__ == "__main__":
    # reader = Reader()

    # if len(sys.argv) != 2:
    #     print("Invalid arguments!")
    #     exit(-1)

    # path = "tests/resources/test_program.rsts"

    # reader.read_file(path)
    # reader.run()

    if "-tv" in sys.argv:
        verify_test()
