#!/usr/bin/env python3

import sys
sys.path.append("../games")

from ..games.engine import engine
from ..games import even


def main():
    engine(even)


if __name__ == "__main__":
    main()