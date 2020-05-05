import sys
from core.reader import Reader
from tests.verify_test import verify_test


def main():
    reader = Reader()

    if len(sys.argv) != 2:
        print("Invalid arguments!")
        exit(-1)

    path = sys.argv[1] 

    try:
        reader.read_file(path)
    except SyntaxError:
        exit(-1)

    reader.run()


if __name__ == "__main__":
    main()
   