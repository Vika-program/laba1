import sys
from src.trans import trans_to_rpn
from src.calc import calc

def run():
    for line in sys.stdin:
        calc(line.rstrip())


if __name__ == '__main__':
    run()
