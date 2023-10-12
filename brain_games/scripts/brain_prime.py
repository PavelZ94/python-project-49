#!/usr/bin/env python3

from ..games.engine import engine
from ..games import prime

import sys
sys.path.append("../games")


def main():
    engine(prime)


if __name__ == "__main__":
    main()
