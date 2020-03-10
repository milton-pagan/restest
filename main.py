from tests.test_test import test_tokens
import sys


if __name__ == '__main__':
	if '-t' in sys.argv:
		print(test_tokens())


