from tests.test_test import test_tokens
import sys
from pprint import pprint


if __name__ == "__main__":
    if "-t" in sys.argv:
        pprint(test_tokens())
