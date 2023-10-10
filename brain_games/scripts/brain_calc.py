#!/usr/bin/env python3

import sys
sys.path.append("../games")

from ..games.engine import engine
from ..games import calc


def main():
    engine(calc)


if __name__ == "__main__":
    main()