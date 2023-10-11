#!/usr/bin/env python3

from ..games.engine import engine
from ..games import calc

import sys
sys.path.append("../games")


def main():
    engine(calc)


if __name__ == "__main__":
    main()
