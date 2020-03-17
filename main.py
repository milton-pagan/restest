
import sys
from pprint import pprint
from tests.print_test import test_tokens



if __name__ == "__main__":
    if "-t" in sys.argv:
        pprint(test_tokens())
