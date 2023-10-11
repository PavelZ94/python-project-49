#!/usr/bin/env python3

from ..games.engine import engine
from ..games import gcd

import sys
sys.path.append("../games")


def main():
    engine(gcd)


if __name__ == "__main__":
    main()
